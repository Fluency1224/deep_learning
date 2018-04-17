#########################################################################
# File Name: save.py
# Author: fluency
# mail: 1005068694@qq.com
# Created Time: Tue 17 Apr 2018 07:46:33 PM CST
#########################################################################
#!/usr/bin/python
#!Coding:utf-8
from sklearn import svm
from sklearn import datasets

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data,iris.target
clf.fit(X, y)


#method1: pickle
#import pickle

#with open('./save/clf.pickle','wb') as f:
#    pickle.dump(clf, f)

#with open('./save/clf.pickle','rb') as f2:
#    clf2 = pickle.load(f2)

#print(clf2.predict(X[0:1]))

#method2:joblib
from sklearn.externals import joblib

#save
joblib.dump(clf,'./save/clf2.pickle')
#restore
clf3 = joblib.load('./save/clf2.pickle')
print(clf3.predict(X[0:1]))

