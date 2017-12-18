#!/usr/bin/python
# _*_ coding: UTF-8 _*_

print('\033[31m=======红============\033[0m')
print('\033[32m=======绿============\033[0m')
print('\033[33m=======黄============\033[0m')
print('\033[34m=======蓝============\033[0m')
print('\033[35m=======粉============\033[0m')
print('\033[36m=======青============\033[0m')

salary = input('\033[34m请输入自己的工资：\033[0m')
while not salary.isdigit():
	print('\033[31m请输入一个整数！\033[0m')
	salary = input('\033[34m请输入自己的工资：\033[0m')

money = int(salary)

goods_list = [ 'book','pen', 'bicycle', 'apple', 'compurter', 'Iphonex', 'MP3']
goods_dict = {
		'book': 10,
		'pen': 3,
		'bicycle':300,
		'apple':8,
		'compurter':5000,
		"Iphoenx":8888,
		'MP3':150
		}
'''
for i in goods_list:
	print(i)

for i in goods_dict:
	print( i, goods_dict[i])
'''
while money > 3:
	print('\033[31m---------------------------------\033[0m')
	print('\033[31m您剩余：\033[0m%d\033[31m元\033[0m' %money)
	for i in goods_dict:
		print( i, goods_dict[i])
	print('\033[31m---------------------------------\033[0m')
	
	goods_name = input('\033[32m请输入要购买的商品名：\033[0m')
	while goods_dict.__contains__('goods_name'):
		print('\033[31m请输入商品列表中的商品！\033[0m')
		goods_name = input('\033[32m请输入要购买的商品名：\033[0m')

	goods_count = input('\033[32m请输入购买的个数：\033[0m')
	while not goods_count.isdigit():
		print('\033[31m请输入一个整数！\033[0m')
		goods_count = input('\033[32m请输入购买的个数：\033[0m')
	
	price = goods_dict.get(goods_name)
	money =money -int(price) * int(goods_count)

print('花完了！')
	
