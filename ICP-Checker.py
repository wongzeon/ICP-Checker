# -*- coding: utf-8 -*-
import os
import re
from requests import get, post
from time import sleep, time
from hashlib import md5
from openpyxl import load_workbook
from openpyxl.workbook import Workbook
from openpyxl.styles import Alignment

class get_require_info(object):
    """
    获取必要的Cookie、Token，以及各类的POST请求由这里的post_tool()完成，
    """
    base_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69',
                'Origin': 'https://beian.miit.gov.cn', 'Referer': 'https://beian.miit.gov.cn/'}

    def __init__(self) -> None:
        self.base_url = 'https://hlwicpfwc.miit.gov.cn/icpproject_query/api/'
        self.auth_url = self.base_url + 'auth' # 返回token
        self.image_url = self.base_url + 'image/getCheckImagePoint' # 返回Secretkey、uuid
        self.check_url = self.base_url + 'image/checkImage' # 返回Sign，传值里的token是uuid
        self.query_url = self.base_url + 'icpAbbreviateInfo/queryByCondition' # 标头需要：cookie、token、sign、uuid

    def post_tool(self, url, data, json, header):
        try:
            response = post(url, data=data, json=json, headers=header, timeout=2)
            response_code = response.json()['code']
            response_msg = response.json()['success']
            if response_code == 200 and response_msg is True:
                return response
            elif response_code == 200 and response_msg is False: # 验证错误，需要重新获取验证图片
                return 'pic_check_fail'
            elif response_code == 401: # Token 过期
                print(f"{' 刷新Token ':-^57}")
                return self.get_token()
            elif response_code == (500 or 501):
                return 'server_error'
            elif response.status_code == 403: # WAF 触发，只有这个会正确返回状态码，其他的错误状态码响应的是200
                print(f"{' 触发防火墙了，过几分钟再试吧 ':*^50}")
                exit()
        except Exception as err:
            return f'error:{err}'

    def get_cookie(self):
        cookie = get(url=self.base_header['Origin'], headers={'User-Agent':self.base_header['User-Agent']}, timeout=1)
        self.base_header.update({'Cookie': cookie.headers['Set-Cookie'].split(';')[0]})

    def get_token(self):
        print(f"\n{' 获取Token中，服务器响应时快时慢 ':-^46}")
        time_stamp = round(time() * 1000)
        auth_key = md5(f'testtest{time_stamp}'.encode('utf-8')).hexdigest()
        auth_data = {'authKey': auth_key, 'timeStamp': time_stamp}
        token_request = self.post_tool(self.auth_url, auth_data, "", self.base_header)
        token_result = token_request.json()['params']['bussiness']
        self.base_header.update({'Token': token_result, 'Accept':'application/json'})
        print(f"\n{' 已获得Token ':-^56}\n")

class file_tool(object):
    """
    文件处理，主要为批量做预留，减少重复代码
    """
    def __init__(self) -> None:
        pass
        
    def file_writer(self, file_path, file_name, file, wr_mode, wr_type):
        with open(f'{file_path}/{file_name}', wr_mode) as f:
            if wr_type == 'write':
                f.write(file)
            else:
                self.file_content = f.read()
                return self.file_content

class query_info(get_require_info, file_tool):
    """
    输入过滤，只对中文输入做过滤，英文域名由于有些域名不在可备案列表内也能备案，所以不做过滤了
    """
    domain_result_list = []
    def __init__(self) -> None:
        super().__init__()

    def regular_input(self):
        print(f"{' 输入 域名/备案号/完整公司名 以查询备案信息 ':-^40}\n")
        info_input = input('查询对象：').replace(' ', '').replace('https://www.', '').replace('http://www.', '').replace('http://', '').replace('www.', '')
        if info_input == '':
             print(f"\n{' 请输入正确域名 ':*^52}\n")
             return -1
        elif '\u4e00' <= info_input <= '\u9fff':
            input_result = re.sub('[^\\u4e00-\\u9fff-A-Za-z0-9,-.()《》—（）]', "", info_input) # 中文输入混入的特殊符号，只允许：-—《》（）().
        else:
            input_result = info_input
        self.query_text = {'pageNum': 1, 'pageSize': 40, 'serviceType': 1, 'unitName': input_result} #serviceType: 1:网站 6:APP 7:小程序 8:快应用

    def query_information(self):
        print(f"\n{' 查询中 ':-^56}")
        icp_info = super().post_tool(self.query_url, '', self.query_text, self.base_header).json()['params']
        total_domains = icp_info['total']
        total_pages = icp_info['lastPage']
        end_row = icp_info['endRow']
        if total_domains == 0:
            print(f"\n{' '+ self.query_text['unitName'] + ' 没有备案信息 ':*^40}\n")
            return -1
        print(f"\n{' '+ self.query_text['unitName'] + ' 共有 ' + str(total_domains) + ' 个备案域名 ':*^40}\n")
        for i in range(total_pages):
            print(f"{' 获取第' + str(i+1) + '页信息 ':-^53}\n")
            for k in range(0, end_row + 1):
                info_base = icp_info['list'][k]
                domain_name = info_base['domain']
                domain_type = info_base['natureName']
                domain_licence = info_base['mainLicence']
                website_licence = info_base['serviceLicence']
                domain_status = info_base['limitAccess']
                domain_approve_date = info_base['updateRecordTime']
                domain_owner = info_base['unitName']
                try:
                    domain_content_approved = info_base['contentTypeName']
                    if domain_content_approved == "":
                        domain_content_approved = "无"
                except KeyError:
                    domain_content_approved = "无"
                row_data = domain_owner, domain_name, domain_licence, website_licence, domain_type, domain_content_approved, domain_status, domain_approve_date
                self.domain_result_list.append(row_data)
            self.query_text.update({'pageNum': i + 2})
            if icp_info['isLastPage'] is True:
                break
            else:
                icp_info = super().post_tool(self.query_url, '', self.query_text, self.base_header).json()['params']
                end_row = icp_info['endRow']
                sleep(3) # 翻页需要慢一点，否则大概率被WAF拦截

class excel_tool(query_info):
    """
    保存结果到Excel文件，注意执行时需关闭“备案信息.xlsx”，否则会保存失败
    """
    def __init__(self) -> None:
        if os.name == 'nt':
            from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER
            key = r'Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders' # 修改过桌面路径的注册表
            target_key = OpenKey(HKEY_CURRENT_USER, key, 0)
            desktop_path = str(QueryValueEx(target_key, 'Desktop')[0])
            if desktop_path == r'%USERPROFILE%\Desktop':
                desktop_path = os.path.join(os.path.expanduser('~'),"Desktop")
        else:
            desktop_path = f'/home/{os.getlogin()}'
            if not os.path.exists(desktop_path):
                os.mkdir(desktop_path)
        self.excel_file_path = desktop_path.replace('\\', '/') + '/备案信息.xlsx'
        super().__init__()

    def set_format(self):
        list_row = len(self.domain_result_list)
        if os.path.exists(self.excel_file_path):
            self.work_book = load_workbook(self.excel_file_path)
            self.work_sheet = self.work_book['备案信息']
            self.start = self.work_sheet.max_row + 1 # 从文件最后一行的后一行开始追加写入
            self.total_row = list_row + self.start
            self.after_title = 0
        else:
            self.work_book = Workbook()
            self.work_sheet = self.work_book.active
            self.work_sheet.title = "备案信息" 
            self.work_sheet.freeze_panes = 'A2' # 冻结窗格
            col_title_list = ['域名主办方', '域名', '备案许可证号', '网站备案号', '域名类型', '网站前置审批项', '是否限制接入', '审核通过日期']
            col_width = {'A': 45, 'B': 30, 'C': 22, 'D': 24, 'E': 9, 'F': 41, 'G': 13, 'H': 21}
            for i in range(8):
                self.work_sheet.cell(1, i + 1).value = col_title_list[i] # 写入表头
            for key, value in col_width.items():
                self.work_sheet.column_dimensions[key].width = value # 设定列宽
            self.start = 0
            self.after_title = 2
            self.total_row = list_row
        self.write_data()
        
    def write_data(self):
        print(f"{' 正在录入信息到表格 ':-^50}\n")
        for i in range(self.start, self.total_row):
            for j in range(8):
                self.work_sheet.cell(i + self.after_title, j + 1).value = self.domain_result_list[i - self.start][j] # 写入数据，对应domain_reuslt_list的数据，结构是：[(1,2,3,4,5,6,7,8),(),()……]
        for row in range(self.work_sheet.max_row):
            for col in range(self.work_sheet.max_column):
                self.work_sheet.cell(row + 1, col + 1).alignment = Alignment(horizontal='center', vertical='center') # 居中对齐
        try:
            self.work_book.save(self.excel_file_path)
        except PermissionError:
            return print("** 备案信息登记表格已打开，无法写入文件。如需写入，请关闭文件后重新执行！ **\n")
        return print(f"{' 查询结果保存在：' + str(self.excel_file_path) + ' ':*^47}\n")

if __name__ == '__main__':
   """
   各类可预期的报错，返回为-1
   """
   os.environ['no_proxy'] = '*'
   query_target = query_info() 
   requirement_info = get_require_info() 
   save_data = excel_tool() 
   print(f"\n{' 项目地址：https://github.com/wongzeon/ICP-Checker ':-^54}\n")
   print(f"{' V2.2.0 2023/11/23 仅用于学习研究，不得用于商业/非法用途 ':-^41}")
   requirement_info.get_cookie() 
   token = requirement_info.get_token() 
   exe_num = 0
   while exe_num <= 2:
        if query_target.regular_input() != -1: 
            if query_target.query_information() != -1: 
                save_data.set_format()
        exe_num += 1 # 控制循环次数han
