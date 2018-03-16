#/usr/bin/env python
#coding:utf-8
import matplotlib.pyplot as plt

#创建窗口
plt.Figure()

#创建小图 2行 2列 第1张
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])
plt.subplot(2,3,4)
plt.plot([0,1],[0,1])
plt.subplot(2,3,5)
plt.plot([0,1],[0,1])
plt.subplot(2,3,6)
plt.plot([0,1],[0,1])



plt.show()