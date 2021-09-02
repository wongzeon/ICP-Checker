# ICP-Checker
一个简单的Python程序，用于查询网站或企业的ICP备案信息

适用于2021年新版的`工信部ICP/IP地址/域名信息备案管理系统`

# 初衷
工作时常需要查询网站的备案信息，总是要打开浏览器、点击书签、完成滑动验证等重复操作，感觉十分浪费时间

原本某工具还是挺方便查询的，结果现在要开通VIP才能查看信息了，实在太坑！

![站长.png](http://ww1.sinaimg.cn/large/61e8a333gy1gqjfsan5qvj20xg0760sv.jpg)

还有就是对Python有兴趣，为了练练手，于是编写了该查询程序。

# 特征
✅ 通过 `https://beian.miit.gov.cn/` 查询信息，确保与管局实际信息一致；

✅ 支持自动完成验证码拖动，存在极低的失败率

✅ 支持循环翻页查询，获取企业名下的所有备案信息

✅ 查询完毕后按任意键继续查询

# 计划
* 将查询结果写入Excel或数据库
* 重构整个程序，完成类和函数封装

# 说明
⚠ 项目仅用于学习交流，不可用于商业及非法用途

# 依赖

Python 版本 => 3.6

`pip install opencv_python`

`pip install requests`

# 实际测试

⏰`最新可用测试时间：2021年7月27日`

![效果.png](http://ww1.sinaimg.cn/large/61e8a333gy1gqjg0q201aj20oy0c6dfw.jpg)

![效果2.png](http://ww1.sinaimg.cn/large/61e8a333gy1gqjfv90ti8j20oc0cz0st.jpg)

![exe运行.png](http://ww1.sinaimg.cn/large/001NakGngy1gsvkys0salj610c0l2tkd02.jpg)

![验证码识别.jpg](http://ww1.sinaimg.cn/large/61e8a333gy1gqjgtbrt35j20dw05agm8.jpg)
