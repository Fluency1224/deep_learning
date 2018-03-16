#/usr/bin/env python
#coding:utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#plot data

#Series
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
#data.plot()
#plt.show()

#DateFrame
data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list("ABCD"))
print(data.head(5))
data = data.cumsum()

#plot methods
#'bar'条形图 'hist','box','kde','area','scatter','hexbin','pie'
#data.plot()
ax = data.plot.scatter(x='A', y='B', color='DarkBlue',label='Class 1')
data.plot.scatter(x='A', y='C', color='DarkGreen',label='Class 2',ax=ax)
plt.show()