from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'http://news.sina.com.cn/'
resp = urlopen(url)   

soup = BeautifulSoup(resp, 'html.parser')

providers = soup.find_all("a", {"target":"_blank", "href":re.compile("http://news.sina.com.cn/s/201")}) + soup.find_all("a", {"target":"_blank", "href":re.compile("http://news.sina.com.cn/o/201")}) + soup.find_all("a", {"target":"_blank", "href":re.compile("http://news.sina.com.cn/w/201")})
# urls = soup.find_all("a", {"target":"_blank", "href":re.compile("http://news.sina.com.cn/s/")})



for provider in providers:
    print(provider.string)
    print(provider['href'])
