#/usr/bin/env python
#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

#柱状图
n = 12
x1 = np.arange(n)
x2 = np.arange(n)
y1 = (1-x1/float(n))*np.random.uniform(0.5,1.0,n)
y2 = (1-x2/float(n))*np.random.uniform(0.5,1.0,n)
#edgecolor边框颜色属性
plt.bar(x1, +y1,edgecolor='white')
plt.bar(x2, -y2,edgecolor='white')

#加文字
for x,y in zip(x1,y1):
    #ha 对齐属性 
    plt.text(x,y + 0.05,'%.2f' % y,ha='center', va='bottom')
    
for x,y in zip(x2,y2):
    #ha 对齐属性 
    plt.text(x,-y - 0.05,'-%.2f' % y,ha='center', va='top')
    
plt.xlim(-.5,n)
plt.ylim(-1.25,1.25)
plt.xticks(())
plt.yticks(())
plt.show()