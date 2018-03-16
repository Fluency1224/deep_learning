#/usr/bin/env python
#coding:utf-8
import numpy as np
#import pandas as pd

#矩阵的属性
array = np.array([[1,2,3],[2,3,4]])
print(array)
print("number of dim:",array.ndim)
print("shape:",array.shape)
print("size:",array.size)

#矩阵的数据类型 dtype
a = np.array([1,2,3],dtype=np.int64)
print(a.dtype)
a.dtype = np.int32
print(a.dtype)
a.dtype = np.int16
print(a.dtype)
a.dtype = np.float
print(a.dtype)

#全0矩阵
b = np.empty((3,4), dtype=int)
print(b)

#矩阵的运算
