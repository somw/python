import requests
from bs4 import BeautifulSoup

url = 'https://www.jobui.com/rank/company/'
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
res=requests.get(url,headers=headers)
print(res.status_code)
soup = BeautifulSoup(res.text,'html.parser')
aa = soup.find_all('ul', class_ = 'textList flsty cfix')
for x in aa:
    a_list = x.find_all('a')
    for y in a_list:
        company_id = y['href']
        url = 'https://www.jobui.com{id}jobs/'
        real_url = url.format(id=company_id)
        res1 = requests.get(real_url,headers=headers)
        print(res1)