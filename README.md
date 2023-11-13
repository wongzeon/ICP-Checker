# 提示

11月13日工信部网站的验证方式发生重大变更，暂无法使用

# ICP-Checker

一个简单的Python程序，用于查询网站或企业的ICP备案信息

适用于~~~2023年新版~~~的`工信部ICP/IP地址/域名信息备案管理系统`

![CentOS](https://img.shields.io/badge/LINUX-CentOS-purple?style=for-the-badge&logo=CentOS)
![Ubuntu](https://img.shields.io/badge/LINUX-Ubuntu-orange?style=for-the-badge&logo=Ubuntu)
![Windows](https://img.shields.io/badge/Windows-7%7C8%7C10%7C11-blue?style=for-the-badge&logo=Windows)
![Python](https://img.shields.io/badge/Python-≥3.6-green?style=for-the-badge&logo=Python)

# 初衷

工作时常需要查询网站的备案信息，总是要打开浏览器、点击书签、完成滑动验证等重复操作，感觉十分浪费时间

原本某工具还是挺方便查询的，结果现在要开通VIP才能查看信息了，实在太坑！于是写了这个小工具。

![站长.png](http://ww1.sinaimg.cn/large/61e8a333gy1gqjfsan5qvj20xg0760sv.jpg)

# 特征

✅ 通过 `https://beian.miit.gov.cn/` 查询信息，确保与管局实际信息一致；

✅ 支持通过域名、公司名、备案号查询备案信息

✅ 支持自动完成拖动验证，存在极低的失败率

✅ 支持循环翻页查询，获取查询到的所有备案信息

✅ 支持将查询结果保存到表格文件

# 使用
已使用Pyinstaller打包成EXE可执行文件，[查看详情](https://github.com/wongzeon/ICP-Checker/releases/tag/2.1.4)

方法一：输入完整的企业名称：XXXX有限公司、XXXX（XXXX）有限公司

方法二：输入不带前缀（如www等）的域名，支持中文域名的查询如：网址之家.cn、小度.中国

方法三：输入备案号查询信息，如："粤B2-20090059-5"、"浙B2-20080224-1"、"京ICP证030173号-1"等，如果不带结尾"-数字"，则会将该证名下所有域名查询出来。

# 计划

* ~~支持将查询结果写入Excel或数据库~~

* ~~重构整个程序，完成函数封装~~

* 制作GUI界面

* 支持批量查询 

# 说明

⚠ 项目仅用于学习交流，不可用于商业及非法用途

结果默认保存：Windows系统保存至桌面，Linux等系统则保存至/home/文件夹

输入域名格式时，会判断域名是否是支持备案的类型，如果提示不支持即代表该域名无法备案

具体可参考工信部公布的[备案域名列表](http://xn--fiq8ituh5mn9d1qbc28lu5dusc.xn--vuq861b/)

# 依赖

如果已经装有 opencv、requests、openpyxl可以跳过这步，如果没有则执行：

`pip install -r requirements.txt`

或分别执行以下命令：

`pip install opencv_python`

`pip install requests`

`pip install openpyxl`

# 实际测试

⏰`最新可用测试时间：2023年9月25日`

![备案查询2.1.9.png](https://pic7.58cdn.com.cn/nowater/webim/big/n_v2e7e7ac7bf769468f82480fc8729d66e0.png)

![beian_info_xlsx.png](https://pic.rmb.bdstatic.com/bjh/539ab061960a8866feb41d88b490355a.png)
