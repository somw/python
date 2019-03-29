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

    list_all = []

    for a in range(len(aa)):
        #print(aa[a].find('em').text)   序号
        #print(aa[a].find('img')['alt'])  电影名
        #print(tes[a].find(class_='rating_num').text)  评分
        #print(comment[a].text)    推荐语
        #print(aa[a].find('a')['href'])   链接
        print(comment[a].text)

        #    print('序号:',aa[a].find('em').text,',电影名:',aa[a].find('img')['alt'],',评分:',tes[a].find(class_='rating_num').text,',推荐语:',comment[a].text,'链接:',aa[a].find('a')['href'])
