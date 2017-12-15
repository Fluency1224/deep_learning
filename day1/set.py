#!/usr/bin/python

student = {'TOM', 'JIM', 'MARY', 'TOM', 'JACK', 'ROSE'}

print(student)

#成员测试
if('ROSE' in student) :
	print('rose在集合中')
else :
	print('rose不在集合中')

#set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
