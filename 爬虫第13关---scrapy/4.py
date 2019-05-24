import requests
from bs4 import BeautifulSoup

start_urls = []
for a in range(2):
    url = 'https://book.douban.com/top250?start='+ str(a *25)
    start_urls.append(url)
    
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    res=requests.get(url,headers=headers)
    # print(res.status_code)
    soup = BeautifulSoup(res.text,'html.parser')
    aa = soup.find('div', class_ = 'indent').find_all('div', class_= 'pl2')
    for x in aa:
        cc = x.find('a')['href']
        url1 = '{id}comments/'
        real_url1 = url1.format(id=cc)
        # print(real_url1)

url2 = 'https://book.douban.com/subject/1770782/comments/'
res1 = requests.get(url2,headers=headers)
# print(res1)
soup1 = BeautifulSoup(res1.text,'html.parser')
bookname = soup1.find('div', id='wrapper').text.split()[0]
dd = soup1.find_all('div',class_='comment')
for b in dd:
    dpid = b.find_all('a')[1].text
    dpcontent = b.find('span',class_='short').text
    print(dpcontent)
