from selenium import webdriver
import time

while True:
    aaa = input('请输入你想要评论的内容，按回车提交：')
    if aaa == '':
        print('&'*5,'评论内容不允许为空','&'*5)
    else:
        break


driver = webdriver.Chrome()
driver.get('https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php')
time.sleep(2)

user = driver.find_element_by_id('user_login')
user.send_keys('spiderman')
pwd = driver.find_element_by_id('user_pass')
pwd.send_keys('crawler334566')
botton = driver.find_element_by_id('wp-submit')
botton.click()
time.sleep(2)


biaoti = driver.find_element_by_partial_link_text('同九义何汝秀')
biaoti.click()

fabiao = driver.find_element_by_id('comment')
fabiao.send_keys(aaa)

aaabotton =driver.find_element_by_id('submit')
aaabotton.click()
time.sleep(2)

driver.close()
print('#' * 6, '评论成功，浏览器已关闭', '#' * 6)