#/usr/bin/env python
#coding:utf-8
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#method 1:subplot2grid 分成一些小格
#创建窗口
plt.Figure()
ax1 = plt.subplot2grid((3,3), (0,0), rowspan=1, colspan=3)
ax1.plot([1,2],[1,2])
ax1.set_title('ax1')
ax2 = plt.subplot2grid((3,3), (1,0), rowspan=2)
ax3 = plt.subplot2grid((3,3), (1,2), colspan=2)
ax4 = plt.subplot2grid((3,3), (2,0))
ax5 = plt.subplot2grid((3,3), (2,1))
#method 2:gridspaec
plt.figure()
gs = gridspec.GridSpec(3,3)
ax1.plot([1,2],[1,2])
ax1.set_title('ax2')
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:2])
ax3 = plt.subplot(gs[1:,2])
ax4 = plt.subplot(gs[-1,0])
ax5 = plt.subplot(gs[-1,-2])
#method 3:easy to define structure
f, ((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex=True,sharey=True)
ax11.set_title('ax3')
ax11.scatter([1,2],[2,1])



plt.tight_layout()
plt.show()