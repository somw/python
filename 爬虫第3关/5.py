import requests
from bs4 import BeautifulSoup

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html,'html.parser')
    aa = soup.find_all('div',class_='item')
    #title = soup.find_all('span',class_='title')
    tes = soup.find_all('div',class_='star')
    comment=soup.find_all('span',class_='inq')
    #url_movie = soup.find('a')['href']
    print(aa)
   