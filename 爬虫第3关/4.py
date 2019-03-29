import requests
from bs4 import BeautifulSoup

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html,'html.parser')
    aa = soup.find_all('div',class_='item')
    for a in aa:
        num = a.find(class_='pic').find('em')
        title = a.find('span',class_='title')
        tes = a.find('span',class_='rating_num')
        comment = a.find('span',class_='inq')
        if comment == None:
            print('无评论')
        else:
            comments=a.find('span',class_='inq')
        url_movie = a.find('a')['href']
    
        print('序号:',num.text,',电影名',title.text,',评分:',tes.text,',推荐语:',comments.text,',链接:',url_movie)