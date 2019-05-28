import requests
from bs4 import BeautifulSoup


url2 = 'https://demo.dscmall.cn/goods.php?id=843'
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
res1 = requests.get(url2,headers=headers)
soup1 = BeautifulSoup(res1.text,'html.parser')
aa = soup1.find('div',class_='summary-basic-info').find('em',id='goods_attr_num').text
print(aa)