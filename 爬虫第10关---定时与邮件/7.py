import requests,csv,random
from bs4 import BeautifulSoup
csv_file = open('top250.csv', 'w', newline = '',encoding='utf-8')
#调用open()函数打开csv文件，传入参数。
writer = csv.writer(csv_file)
#用csv.writer()函数创建一个对象
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url)
    #解析网页
    soup = BeautifulSoup(res.text,'html.parser')
    bs = soup.find('ol',class_='grid_view').find_all('li')
    for aa in bs:
        title = aa.find('span',class_='title')
        lists = [title]
        print(lists)