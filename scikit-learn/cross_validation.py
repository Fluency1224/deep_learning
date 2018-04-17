#########################################################################
# File Name: cross_validation.py
# Author: fluency
# mail: 1005068694@qq.com
# Created Time: Tue 17 Apr 2018 04:27:34 PM CST
#########################################################################
#!/usr/bin/python
#!Coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score

iris = datasets.load_iris()
X = iris.data
y = iris.target


#X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=4)
#knn = KNeighborsClassifier(n_neighbors=5)
#knn.fit(X_train,y_train)
#y_pred = knn.predict(X_test)
#print(knn.score(X_test, y_test))

knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn,X,y,cv=5,scoring='accuracy')
print(scores.mean())

k_range = range(1,31)
k_scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy')
    loss = -cross_val_score(knn,X,y,cv=10,scoring='mean_squared_error')
    k_scores.append(loss.mean())


plt.plot(k_range,k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross Validation Accuracy')
plt.show()
