# WestWorld-auto-download-email-xunlei-



	# -*- coding: utf-8 -*-
	# python 3.5.2
	# 测试系统，Win10
	# Author:Van
	# 实现《西部世界》有更新后自动下载，以及邮件通知
	# V1.0
	# 欢迎各种改进意见
	# 请把对应的帐号密码修改成自己的


----------

	# -*- coding: utf-8 -*-
	# python 3.5.2
	# tested on Win10
	# Author:Van
	# WestWorld auto email notice and xunlei download
	# V1.0
	# welcome to improve it
	# modify the account information as yours


3、代码分析，其中用到了deepcopy，这个功能很有用，并配合了2个数组的差集，使得可以规避定时器，而让脚本直接比较temp_link的内容，而扑捉到网站有新的更新了。在地址识别的时候，一开始用.xpath 没显示内容，有点奇怪，后来根据特性，使用了strats_with识别了内容。另外，原始的邮件发送函数，是一个接收人，如果要多发，则receiver的格式为list，并修改 msg['To'] = ','.join(receiver)

4、邮件的作用是可以利用微信绑定来推送，相对短信，更觉方便。



5、感谢： 
 @陌 提供了163发送email的代码
 @何方 提供了高清网站源
 @其他人，交流了细节

6、可改进点：
邮件的地址内容显示的是一个列表，有待改进。