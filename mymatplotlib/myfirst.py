#/usr/bin/env python
#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
#matplotlib的基本用法

x = np.linspace(-1, 1, 50)
#y = 2*x+1
y= x**2
plt.plot(x,y)
plt.show()
