import requests
from bs4 import BeautifulSoup
res = requests.get('http://books.toscrape.com')
html = res.text
soup = BeautifulSoup(html,'html.parser')
aa = soup.find('ul',class_='nav').find('ul').find_all('li')
#print(aa)
for a in aa:
    bb = a.find('a')
    print(bb.text.strip())