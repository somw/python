import requests
from bs4 import BeautifulSoup
res = requests.get('https://wordpress-edu-3autumn.localprod.forc.work')
html = res.text
soup = BeautifulSoup(html,'html.parser')
aa = soup.find_all('header',class_='entry-header')
for a in aa:
    titles = a.find('h2',class_='entry-title').find('a')
    times = a.find('a').find('time')
    links = a.find('a')
    print('文章标题:',titles.text,'\n','发布时间:',times.text,'\n','文章链接:',links['href'],'\n----------')
    