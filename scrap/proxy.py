import urllib.request
from bs4 import BeautifulSoup
import re
#通过代理去爬取网站 代理ip网站 http://www.xicidaili.com/
def use_proxy(url,proxy_addr):
    proxy = urllib.request.ProxyHandler({"http":proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    return data

proxy_addr = "114.226.105.154:6666"
url = "https://www.csdn.net/nav/iot"
data = use_proxy(url, proxy_addr)
soup = BeautifulSoup(data, 'html.parser')
atricles = soup.findAll("a", {"target":"_blank", "href":re.compile("https://blog.csdn.net/.*?/article/details/")})

# urls = soup.find_all("a", {"target":"_blank", "href":re.compile("http://news.sina.com.cn/s/")})

for atricle in atricles:
    if(atricle.string != None):
        print(atricle.string)
        print(atricle['href'])
