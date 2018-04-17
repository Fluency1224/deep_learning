#########################################################################
# File Name: datasets.py
# Author: fluency
# mail: 1005068694@qq.com
# Created Time: Tue 17 Apr 2018 02:58:38 PM CST
#########################################################################
#!/usr/bin/python
#!Coding:utf-8
import matplotlib.pyplot as plt
import numpy as py
from sklearn import datasets
from sklearn.linear_model import LinearRegression

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

model = LinearRegression()
model.fit(data_X, data_y)

print(model.predict(data_X[:4,:]))
print(data_y[:4])

X, y = datasets.make_regression(n_samples=100, n_features=1,n_targets=1,noise=10)

plt.scatter(X,y)
plt.show()
