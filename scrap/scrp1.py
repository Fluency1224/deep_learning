#########################################################################
# File Name: scrp1.py
# Author: fluency
# mail: 1005068694@qq.com
# Created Time: Tue 10 Apr 2018 11:45:36 AM CST
#########################################################################
#!/usr/bin/python
#!Coding:utf-8
from urllib.request import urlopen

#if has chinese, apply decode()
html = urlopen (
        "http://morvanzhou.github.io/tutorials/data-manipulation/scraping/"
).read().decode('utf-8')
print(html)

