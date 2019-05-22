from gevent import monkey
monkey.patch_all()
import gevent, requests, bs4, csv
from gevent.queue import Queue

csv_file = open('boohee.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(['食物','热量','链接'])

word = Queue()
url1 = 'http://www.boohee.com/food/group/{type}?page={page}'
for a in range(1,4):
    for b in range(1,4):
        real_url = url1.format(type=a, page=b)
        word.put_nowait(real_url)

url2 = 'http://www.boohee.com/food/view_menu?page={page}'
for c in range(1,4):
    cc_url = url2.format(page=c)
    word.put_nowait(cc_url)

def aa():
    while not word.empty():
        url = word.get_nowait()
        res = requests.get(url)
        bs_res = bs4.BeautifulSoup(res.text, 'html.parser')
        foods = bs_res.find_all('li',class_='item clearfix')
        for d in foods:
            food_name = d.find_all('a')[1]['title']
            food_reliang = d.find('p').text
            food_link = 'http://www.boohee.com' + d.find_all('a')[1]['href']
            writer.writerow([food_name,food_reliang,food_link])

task_list = []
for x in range(5):
    task = gevent.spawn(aa)
    task_list.append(task)
gevent.joinall(task_list)
 

