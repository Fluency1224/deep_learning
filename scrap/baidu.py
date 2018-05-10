#########################################################################
# File Name: baidu.py
# Author: fluency
# mail: 1005068694@qq.com
# Created Time: Tue 10 Apr 2018 07:08:48 PM CST
#########################################################################
#!/usr/bin/python
#!Coding:utf-8
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re 
import random

base_url = "http://baike.baidu.com"
his = ["/item/%e7%bd%91%e7%bb%9c%e7%88%ac%e8%99%ab"]

for i in range(20):
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='html.parser')
    print(soup.find('h1').get_text(), 'url:', his[-1])

    #find valid urls
    sub_urls = soup.find_all("a", {"target":"_blank", "href":re.compile("/item/(%.{2})+$")})
    #print(sub_urls)

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        #no valid sub link found
        his.pop()
    #print(his)

