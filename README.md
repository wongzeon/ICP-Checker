# ICP-Checker

一个简单的Python程序，用于查询网站或企业的ICP备案信息

适用于2023年新版的`工信部ICP/IP地址/域名信息备案管理系统`

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

✅ 支持循环翻页查询，获取查询到的所有备案信息

✅ 支持将查询结果保存到表格文件

# 使用
已使用Pyinstaller打包成EXE可执行文件，[查看详情](https://github.com/wongzeon/ICP-Checker/releases/tag/2.2.0)

方法一：输入完整的企业名称：XXXX有限公司、XXXX（XXXX）有限公司

方法二：输入不带前缀（如www等）的域名，支持中文域名的查询如：网址之家.cn、小度.中国

方法三：输入备案号查询信息，如："粤B2-20090059-5"、"浙B2-20080224-1"、"京ICP证030173号-1"等，如果不带结尾"-数字"，则会将该证名下所有域名查询出来。

# 计划

* 支持批量查询 

# 说明

⚠ 项目仅用于学习交流，不可用于商业及非法用途

结果默认保存：Windows系统保存至桌面，Linux等系统则保存至/home/用户名文件夹

2.2版本开始，仅对中文输入信息过滤，允许特殊符号为：. - 《》（）() — ，如果需要增加，可自行在第89行过滤规则内增加

# 依赖

`pip install -r requirements.txt`

# 实际测试

⏰`最新可用测试时间：2023年11月23日`

![备案查询V2.2.0](https://pic1.58cdn.com.cn/nowater/webim/big/n_v2787194d15b564c00941d20fb5fdf6788.png)
![2023-11-23](https://pic8.58cdn.com.cn/nowater/webim/big/n_v2a2b7aab92ca84922ab827b49f2b016de.png)
