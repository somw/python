import requests
from bs4 import BeautifulSoup

ids= ['1105','1115','1129','1145','1160','347','463','630','547','1142','353','355','357','359','360','362','3','4','5','860']
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
for x in range(20):
    real_url = 'https://demo.dscmall.cn/category.php?id='+ids[x]
    res = requests.get(real_url,headers=headers)
    # print(res.status_code)
    soup =BeautifulSoup(res.text, 'html.parser')
    aa = soup.find_all('div', class_='gl-i-wrap')
    for a in aa:
        bb = a.find('div','p-img').find('a')['href']
        url1 = 'https://demo.dscmall.cn/{goods}'
        real_url1 = url1.format(goods=bb)

url2 = 'https://demo.dscmall.cn/goods.php?id=843'
res1 = requests.get(url2,headers=headers)
soup1 = BeautifulSoup(res1.text,'html.parser')
