from gevent import monkey
monkey.patch_all()
# monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步   
import gevent,requests,time
from gevent.queue import Queue

start = time.time()

url_list = ['https://www.baidu.com/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']

work = Queue() #创建队列对象，并赋值给work
for a in url_list:
    work.put_nowait(a)  #用put_nowait()函数可以把网址都放进队列里

def bb():
    while not work.empty():  #当队列不是空的时候，就执行下面的程序
        cc = work.get_nowait()  #用get_nowait()函数可以把队列里的网址都取出
        res = requests.get(cc)
        print(cc, work.qsize(),res.status_code)

dd_list = []
for x in range(2):  #相当于创建了2个爬虫
    dd = gevent.spawn(bb)  #用gevent.spawn()函数创建执行bb()函数的任务
    dd_list.append(dd)  #往任务列表添加任务
gevent.joinall(dd_list) #用gevent.joinall()方法，执行任务列表里的所有任务，就是让爬虫开始爬取网站

end = time.time()
print(end-start)
