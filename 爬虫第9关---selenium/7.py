from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)

teacher = driver.find_element_by_id('teacher')
teacher.send_keys('酱酱')
assistant = driver.find_element_by_id('assistant')
assistant.send_keys('都喜欢')
botton = driver.find_element_by_class_name('sub')
botton.click()
time.sleep(2)

pageSource = driver.page_source
soup = BeautifulSoup(pageSource,'html.parser')
content = soup.find_all(class_='content')
for aa in content:
    biaoti = aa.find('h1').text
    neirong = aa.find('p').text.replace('  ','')
    print( biaoti + '\n' + neirong + '\n')
driver.close()