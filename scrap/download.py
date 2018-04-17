#########################################################################
# File Name: download.py
# Author: fluency
# mail: 1005068694@qq.com
# Created Time: Tue 10 Apr 2018 08:03:01 PM CST
#########################################################################
#!/usr/bin/python
#!Coding:utf-8
import os
import urllib.request as url2
import requests

os.makedirs('./img/', exist_ok=True)
#要下载文件的URL
img_url = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"

#下载文件 retrieve 
url2.urlretrieve(img_url, './img/image.png')

#下载文件 requests方法
r = requests.get(img_url)

with open('./img/image2.png','wb') as f:
    f.write(r.content)

#下载文件 下载一个很大的文件 分段下载
r = requests.get(img_url, stream=True)

with open('./img/image3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)

