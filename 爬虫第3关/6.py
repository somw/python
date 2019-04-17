import requests
from bs4 import BeautifulSoup
from urllib.request import quote
#quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开
res = requests.get('https://www.ygdy8.com')
res.encoding = 'gbk'
html = res.text
soup = BeautifulSoup(html,'html.parser')
aa = soup.find_all('div',class_='searchl')


names = soup.find('input')['value'][15:]

name = input('输入电影名：%s' % names)


url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(name)


res1 = requests.get(url)
html1 = res1.text
soup1 = BeautifulSoup(html,'html.parser')
bb = soup1.find_all('div',class_='co_content8')

for b in bb:
    print(bb[b].find('a')['href'])
