import requests
from bs4 import BeautifulSoup

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
print(res.status_code) #检查请求是否正确响应
html = res.text
aa = BeautifulSoup(html,'html.parser') #把网页解析为BeautifulSoup对象
bb = aa.find_all(class_='books')
for cc in bb:
    kind = cc.find('h2') # 在列表的每个元素里，匹配标签<h2>提取出数据
    title = cc.find(class_='title') #匹配标签class='title'提取出数据
    info = cc.find(class_='info')
    #print(kind,'\n',title,'\n',info) #打印提取出的数据
    #print(type(kind),type(title),type(info)) #打印提取出的数据类型
    print(kind.text,'\n',title['href'],'\n',info.text)