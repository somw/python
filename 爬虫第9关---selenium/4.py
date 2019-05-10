from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome()

driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html')
time.sleep(2)

#comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li')

button = driver.find_element_by_class_name('js_get_more_hot')
button.click()
time.sleep(2)

pageSource = driver.page_source  #获取exement渲染完成的网页源代码
soup = BeautifulSoup(pageSource,'html.parser') #使用bs解析网页
coms = soup.find('ul',class_='js_hot_list').find_all('li',class_='js_cmt_li')  #使用bs提取元素

print(type(coms))
print(len(coms))
for a in coms:
    sweet = a.find('p')
    print('评论：%s\n---\n'%sweet.text)
driver.close()