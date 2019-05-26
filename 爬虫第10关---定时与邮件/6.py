import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import schedule,time

account = input('请输入你的电子邮箱：')
password = input('请输入你的密码：')   #请输入你的密码：lktqzpxrylgwbfh
recipien = input('请输入收件人的电子邮箱：')

def foods():
    res_foods = requests.get('http://www.xiachufang.com/explore/') #获取url的数据，返回一个respos对象，赋值给res_foods
    bs_foods = BeautifulSoup(res_foods.text,'html.parser') #先把res_foods解析为字符串，再把网页解析为BeautifulSoup对象
    foods_list = bs_foods.find_all('div',class_='info pure-u') #通过匹配属性class='info pure-u'提取出我们想要的元素

    list_all = ''
    num = 0
    for a in foods_list:  #遍历列表foods_list
        num = num + 1
        tag_a = a.find('a')  #在列表中的每个元素里，匹配标签<a>提取出数据
        foods_name = tag_a.text.strip()  #把名字两边空格清除
        #foods_name = a.find('a').text.replace('','')
        foods_url = 'http://www.xiachufang.com/'+ tag_a['href']  #在列表中的每个元素里，匹配属性href = ''提取出数据

        tag_p = a.find('p',class_='ing ellipsis') #在列表中的每个元素里，匹配属性calss_='ing ellipsis'提取出数据
        ingellipsis = tag_p.text[1:-1]
        list_info = '''
            序号：%s
            菜名：%s
            链接：%s
            原料：%s
        ''' %(num,foods_name,foods_url,ingellipsis)
        list_all = list_all + list_info
    return(list_all)

def emails(list_all):
    global account,password,recipien
    mailhost = 'smtp.qq.com'  #把QQ邮箱的服务器地址赋值到变量mailhost,地址应为字符串格式
    qqmail = smtplib.SMTP()  #实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的属性和方法了
    qqmail.connect(mailhost,25)  #连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。
    qqmail.login(account,password)
    content = '亲爱的，本周的热门热菜如下' + list_all
    message = MIMEText(content,'plain','utf-8')
    subject = '周末吃什么'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        qqmail.sendmail(account, recipien, message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    qqmail.quit()

def job():
    print('开始第一次任务')
    list_all = foods() #创建一个实例化
    emails(list_all) 
    print('任务完成')

schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)