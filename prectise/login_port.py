#!/usr/bin/python
import time

name = '刘胖'
passwd = '123456'
count = 0

while True:
	uname = input('\033[34m请输入用户名：\033[0m')
	upasswd = input('\033[34m请输入密码：\033[0m')
	if count == 2:
		print('\033[31m程序锁死！请等待10秒再次输入!\033[0m')
		time.sleep(10)
		count = 0
		continue
	if (uname == name) and (upasswd == passwd):
		print('\033[31m恭喜登陆成功\033[0m')
		break
	else :
		count += 1
		print('\033[32m你还剩%d次尝试机会！\033[0m', 3 - count)
		

