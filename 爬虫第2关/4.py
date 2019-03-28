import requests
from bs4 import BeautifulSoup
res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
html = res.text
soup = BeautifulSoup(html,'html.parser')
aa = soup.find_all(class_='product_pod')
#print(aa)
for a in aa:
    title = a.find('h3').find('a')
    price = a.find('p',class_='price_color')
    star =a.find('p',class_='star-rating')
    print('书名：',title['title'],'\n价格：',price.text,'\n评分：',star['class'][1],'\n----------')