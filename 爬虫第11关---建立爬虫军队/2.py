from gevent import monkey
monkey.patch_all()
import gevent,requests,time

start = time.time()

url_list = ['https://www.baidu.com/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']

def aa(url):
    r = requests.get(url)
    print(url,time.time()-start,r.status_code)

bb_list = []
for a in url_list:
    bb = gevent.spawn(aa,a)   #用gevent.spawn()函数创建任务
    bb_list.append(bb)  #往任务列表添加任务

gevent.joinall(bb_list) #执行任务列表里的所有任务，就是让爬虫开始爬取网站

end = time.time()
print(end-start)