from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'https://read.douban.com/provider/all'
resp = urlopen(url)   

soup = BeautifulSoup(resp, 'html.parser')

providers = soup.findAll('div', class_="name")

for provider in providers:
    print(provider.string)

