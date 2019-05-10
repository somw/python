from selenium import webdriver
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

content = driver.find_elements_by_class_name('content')
for aa in content:
    biaoti = aa.find_element_by_tag_name('h1').text
    neirong = aa.find_element_by_tag_name('p').text
    print( biaoti + '\n' + neirong + '\n')
driver.close()
