#/usr/bin/env python
#coding:utf-8

import pandas as pd
import numpy as np

dates = pd.date_range('20180308',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(dates)
print(df)
print('-------------select--------------------------')
#输出某一列
print(df['A'])
print(df.A)
#选择某列
print(df[0:3])

#select by label:loc 以标签进行数据选择
print(df.loc['20180309'])
print(df.loc[:,['A','C']])
print(df.loc['20180309',['A','C']])
#select by position:iloc 以位置进行数据选择
print(df.iloc[3:4,1:2])
#mixed selection:ix
print(df.ix[1:3,['A','D']])
#boolean indexing
print(df[df.A>8])
print('------------set value---------------------------')
#对dateframe中的值进行修改
df.iloc[2,2] = 1111
print(df)
df.loc['20180310',['C']] = 2222
print(df)
df.A[df.A>12] = 0
print(df)
df[df.A>8] = 0
print(df)
df['F'] = np.nan
print(df)
df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20180308',periods=6))
print(df)
print('-------------------operation--------------------------------')
dates1 = pd.date_range('20180308',periods=6)
df1 = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates1,columns=['A','B','C','D'])
df1.iloc[0,1] = np.nan
df1.iloc[1,2] = np.nan
print(dates1)
print(df1)
#数据选择丢弃 有nan的数据 axis属性丢行或者列 how={'any','all'} all是所有数据都为nan才丢弃
print(df1.dropna(axis=0,how='any'))
#处理nan数据
print(df1.fillna(value=11111))
#判断数据是否缺失
print(df1.isnull())
print(np.any(df1.isnull) == True)








