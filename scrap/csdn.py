from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


url = 'https://www.csdn.net/nav/iot'
resp = urlopen(url)   

soup = BeautifulSoup(resp, 'html.parser')

atricles = soup.findAll("a", {"target":"_blank", "href":re.compile("https://blog.csdn.net/.*?/article/details/")})

# urls = soup.find_all("a", {"target":"_blank", "href":re.compile("http://news.sina.com.cn/s/")})

for atricle in atricles:
    if(atricle.string != None):
        print(atricle.string)
        print(atricle['href'])

   