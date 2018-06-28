from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'http://www.xicidaili.com/'
resp = urlopen(url)   

soup = BeautifulSoup(resp, 'html.parser')

proxy_ip = soup.findAll("td")

# urls = soup.find_all("a", {"target":"_blank", "href":re.compile("http://news.sina.com.cn/s/")})

for atricle in atricles:
    if(atricle.string != None):
        print(atricle.string)
        print(atricle['href'])