#/usr/bin/env python
#coding:utf-8
import pandas as pd
import numpy as np

#数据的读取和导出
data = pd.read_csv('student.csv')
print(data)
data.to_pickle('student.pickle')
data1 = pd.read_pickle('student.pickle')
print(data1)
#数据的合并 concatenating
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
print(df1,'\n',df2,'\n',df3)
#上下合并 ignore_index 重新排序属性
res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res)
print('------------------------------------')
df4 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df5 = pd.DataFrame(np.ones((3,4))*1,columns=['b','d','c','e'],index=[2,3,4])
print(df4,'\n',df5)
#join,['inner','outer']
res1 = pd.concat([df4,df5], join='outer')
print(res1)
res1 = pd.concat([df4,df5], join='inner')
print(res1)
#join_axes 左右合并 按照指定的
res1 = pd.concat([df4,df5], axis=1, join_axes=[df4.index])
print(res1)
print('------------------------------------')
#append
print(df1,'\n',df2)
res = df1.append([df2,df3],ignore_index=True)
print(res)
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res = df1.append(s1,ignore_index=True)
print(res)
