# ICP-Checker

一个简单的Python程序，用于查询网站或企业的ICP备案信息

适用于2022年新版的`工信部ICP/IP地址/域名信息备案管理系统`

# 初衷

工作时常需要查询网站的备案信息，总是要打开浏览器、点击书签、完成滑动验证等重复操作，感觉十分浪费时间

原本某工具还是挺方便查询的，结果现在要开通VIP才能查看信息了，实在太坑！于是写了这个小工具。

![站长.png](http://ww1.sinaimg.cn/large/61e8a333gy1gqjfsan5qvj20xg0760sv.jpg)

# 特征

✅ 通过 `https://beian.miit.gov.cn/` 查询信息，确保与管局实际信息一致；

✅ 支持自动完成拖动验证，存在极低的失败率

✅ 支持循环翻页查询，获取企业名下的所有备案信息

✅ 支持将查询结果保存到表格文件

✅ 查询完毕后按任意键继续查询

# 使用

方法一：输入完整的企业名称：XXXX有限公司、xxxx(xxx)有限公司

方法二：输入不带前缀（如www等）的域名，支持中文域名的查询如：网址之家.cn、小度.中国

# 计划

* ~~支持将查询结果写入Excel或数据库~~

* ~~重构整个程序，完成函数封装~~

* 制作GUI界面

# 说明

⚠ 项目仅用于学习交流，不可用于商业及非法用途

结果默认保存：Windows系统保存至桌面，Linux等系统则保存至/home/文件夹

输入域名格式时，会判断域名是否是支持备案的类型，如果提示不支持即代表该域名无法备案

具体可参考工信部公布的[备案域名列表](http://xn--fiq8ituh5mn9d1qbc28lu5dusc.xn--vuq861b/)

# 依赖

Python 版本 => 3.6

如果已经装有 opencv、requests、openpyxl可以跳过这步，如果没有则执行：

`pip install -r requirements.txt`

或分别执行以下命令：

`pip install opencv_python`

`pip install requests`

`pip install openpyxl`

# 实际测试

⏰`最新可用测试时间：2022年5月6日`

![beian_info.png](https://pic.rmb.bdstatic.com/bjh/5ffd54074744c80343a8e466fcd76be0.png)

![beian_info_xlsx.png](https://pic.rmb.bdstatic.com/bjh/539ab061960a8866feb41d88b490355a.png)

![验证码识别.jpg](http://ww1.sinaimg.cn/large/61e8a333gy1gqjgtbrt35j20dw05agm8.jpg)
