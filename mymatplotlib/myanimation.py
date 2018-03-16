#/usr/bin/env python
#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm

#动图
fig, ax = plt.subplots()
x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))

def animation(i):
    line.set_ydata(np.sin(x+1/100))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,

ani = anm.FuncAnimation(fig=fig, func=animation, frames=100,init_func=init,interval=120,blit=False)

plt.show()