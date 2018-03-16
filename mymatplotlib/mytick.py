#/usr/bin/env python
#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = 0.1*x

#窗口定义
plt.figure()
plt.plot(x, y,linewidth=10)
plt.ylim(-2,2)
#坐标轴删除和移动
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

#tcik 
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='red',edgecolor='None',alpha=0.3))   

plt.show()