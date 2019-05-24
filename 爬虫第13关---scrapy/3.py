import requests
from bs4 import BeautifulSoup

url = 'https://www.jobui.com/rank/company/'
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
res=requests.get(url,headers=headers)
# print(res.status_code)
soup = BeautifulSoup(res.text,'html.parser')
aa = soup.find_all('ul', class_ = 'textList flsty cfix')
for x in aa:
    a_list = x.find_all('a')
    print(a_list)
    for y in a_list:
        company_id = y['href']
        url = 'https://www.jobui.com{id}jobs/'
        real_url = url.format(id=company_id)

url1 = 'https://www.jobui.com/company/15110/jobs/'
res1 = requests.get(url1,headers=headers)
print(res1.status_code)
soup1 = BeautifulSoup(res1.text,'html.parser')
company = soup1.find('h1',id='companyH1').text.strip()
print(company)
cc = soup1.find_all('div', class_='job-simple-content')
for a in cc:
    position = a.find('a', class_ = 'job-name').find('h3').text
    dd = a.find('div', class_ = 'job-desc')
    spanall = dd.findAll('span')
    address = spanall[0].text
    detail = spanall[1].text
#     print(address+','+detail)