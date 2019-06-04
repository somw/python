import requests,csv,random
from bs4 import BeautifulSoup
from urllib.request import quote

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
        title = aa.find('span',class_='title').text
        lists = [title]
        writer.writerow(lists)
csv_file.close()

movielist = []
csv_file = open('top250.csv','r',newline='',encoding='utf-8')
reader = csv.reader(csv_file)
for bb in reader:
    movielist.append(bb[0])
# 以上，为读取豆瓣电影Top250榜单的csv文件，并写入列表movielist中
three_list = random.sample(movielist,3)
# 以上，是从列表movielist中，随机抽取三部电影，取出来的是一个列表。
# print(three_list)
for cc in three_list:
    gbkcc = cc.encode('gbk')
    searchurl = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(gbkcc)
    res = requests.get(searchurl)
    res.encoding = 'gbk'
    soup_movie = BeautifulSoup(res.text, 'html.parser')
    bs = soup_movie.find('div', class_ = 'co_content8').find_all('table')
    if bs:
        bs1 = bs[0].find('a')['href']
        movieurl = 'https://www.ygdy8.com/' + bs1
        res1 = requests.get(movieurl)
        res1.encoding = 'gbk'
        soup_movies = BeautifulSoup(res1.text,'html.parser')
        downloadurl = soup_movies.find('div', id='Zoom').find('span').find('table').find('a')['href']
        content = cc + '\n' + downloadurl
    else:
        contents = '没有' + cc + '的下载链接'
        print(contents)