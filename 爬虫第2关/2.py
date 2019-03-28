import requests #导入requests
from bs4 import BeautifulSoup

res = requests.get('https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/')
print(res.status_code) #检查请求是否正确响应
html = res.text 
soup = BeautifulSoup(html,'html.parser') #把网页解析为BeautifulSoup对象
aa = soup.find_all(class_='comment-content')
#print(aa)
for a in aa:
    plun = a.find('p')
    print(plun.text,'\n')