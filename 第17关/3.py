#用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import csv


from_addr = input("请输入邮箱账号：")
password = input("请输入邮箱授权码：")
smtp_server = 'smtp.qq.com'

text='''
亲爱的朋友：
    我是洺洺，人生苦短，来跟我一起学习python吧
    洺洺
    2019.03.19
'''


data = [['somw','somw@qq.com'],['zhai','zhai817@126.com']]

#写入收件人数据
with open(r'd:\python\第17关\to_attrs.csv','w',newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

#读取收件人数据，并启动写信和发送流程
with open(r'D:\python\第17关\to_attrs.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        to_addrs = row[1]
        msg = MIMEText(text,'plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addrs)
        msg['Subject'] = Header('打扰你了，这是群发。')
        #开启发信服务，这里使用的是加密传输
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server,465)
        #登录发信邮箱
        server.login(from_addr,password)
        #发送邮件
        server.sendmail(from_addr, to_addrs, msg.as_string())

#关闭服务器
server.quit()