import requests
from bs4 import BeautifulSoup
import smtplib 
from email.mime.text import MIMEText
from email.header import Header
import schedule
import time

def weather_spider():
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url='http://www.weather.com.cn/weather/101280601.shtml'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    data1= soup.find(class_='tem')
    data2= soup.find(class_='wea')
    tem=data1.text
    weather=data2.text
    return tem,weather

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver=input('请输入收件人的邮箱：')
#请输入你的密码：oapjxyjhifrqbej
def send_email(tem,weather):
    global account,password,receiver
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    qqmail.login(account,password)
    
    content='亲爱的，今天的天气是：'+tem+weather
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '今日天气预报'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
        qqmail.quit()

def job():
    print('开始一次任务')
    tem,weather = weather_spider()
    send_email(tem,weather)
    print('任务完成')

# schedule.every().day.at("17:06").do(job) 
# while True:
#     schedule.run_pending()
#     time.sleep(1)