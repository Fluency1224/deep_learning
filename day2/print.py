#!/usr/bin/python

var1 = input('input var1:')
var2 = input('input var2:')
var3 = input('input var3:')

print ('''
==============================
	你好
	这里是格式化输出
这里是测试
		var1 = %s
		var2 = %s
		var3 = %s
==============================
''' % (var1, var2, var3))

print ('\033[31;1m颜色实验')
print ('\033[32;1m颜色实验')
print ('\033[33;1m颜色实验')
print ('\033[34;1m颜色实验')
print ('\033[35;1m颜色实验')
print ('\033[36;1m颜色实验')

