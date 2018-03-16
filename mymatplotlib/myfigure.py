#/usr/bin/env python
#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 1000)
y1 = 2*x+1
y2 = x**2
#通过不同的窗口显示 
plt.figure()
#plt.plot(x,y1)
#plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

#坐标轴的显示参数
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3,],
           [r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])

#修改坐标轴的位置
#gca = 'get current axis'
#删除右边和上边的坐标线
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#移动x y坐标轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.show()
