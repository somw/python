import requests
from bs4 import BeautifulSoup
from urllib.request import quote
#quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开
name = input('输入电影名：')
gbkname=name.encode('gbk')
url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(gbkname)
#print(url)

res = requests.get(url)
res.encoding='gbk'
html = res.text
soup = BeautifulSoup(html,'html.parser')
bb = soup.find(class_='co_content8').find_all('table')
#print(bb)

if bb:
    bb = bb[0].find('a')['href']
    bburl = 'https://www.ygdy8.com/'+bb
    res1 = requests.get(bburl)
    res1.encoding = 'gbk'
    bb_soup = BeautifulSoup(res1.text,'html.parser')
    urldownload = bb_soup.find('div',id="Zoom").find('span').find('table').find('a')['href']
    print(urldownload) 
else:
    print('没有' + name)