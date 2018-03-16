#/usr/bin/env python
#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

#散点图
n = 1024
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
#for color value
t = np.arctan2(y,x) 
plt.scatter(x,y,s=70,c=t,alpha=0.5)
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.xticks(())
plt.yticks(())
plt.show()