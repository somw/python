#提示：
#1.分析数据存在哪里（打开“检查”工具，刷新页面，查看第0个请求，看【response】）
#2.观察网址规律（多翻几页，看看网址会有什么变化）
#3.获取、解析和提取数据（需涉及知识点：queue、gevent、request、BeautifulSoup、find和find_all）
#4.存储数据（csv本身的编码格式是utf-8，可以往open（）里传入参数encoding='utf-8'。这样能避免由编码问题引起的报错。)
#注：在练习的【文件】中，你能找到自己创建的csv文件。将其下载到本地电脑后，请用记事本打开，因为用Excel打开可能会因编码问题出现乱码
from gevent import monkey
monkey.patch_all()
# monkey.patch_all()能把程序变成协助式运行，就是可以帮助程序实现异步
import gevent, requests,bs4,csv
from gevent.queue import Queue

csv_file = open('timetop.csv','w',newline='', encoding = 'utf-8')
writer = csv.writer(csv_file)

word = Queue()
url1 = 'http://www.mtime.com/top/tv/top100/'
word.put_nowait(url1)

url2 = 'http://www.mtime.com/top/tv/top100/index-{page}.html'
for a in range(2,11):
    real_url2 = url2.format(page=a)
    word.put_nowait(real_url2)

def aa():
    while not word.empty():
        url = word.get_nowait()
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text,'html.parser')
        bb = soup.find('ul',id='asyncRatingRegion').find_all('div',class_='mov_con')
        for b in bb:
            title = b.find('a').text
            data = b.find_all('p')
            TV_data = ''
            for c in data:
                TV_data = TV_data + '/' + c.text.replace('&nbsp;','').replace(' ','')
            writer.writerow([title,TV_data])

task_list = []
for i in range(3):
    task = gevent.spawn(aa)
    task_list.append(task)
gevent.joinall(task_list)
