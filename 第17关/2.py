# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 发信方的信息：发信邮箱，qq邮箱授权码
from_addr = input("请你输入登录邮箱：")
password = input("请你输入邮箱授权码：")

# 收信方邮箱
to_addrs = [] 
while True:
    a = input("请你输入收件邮箱：")
    #输入收件人邮箱
    to_addrs.append(a)
    #写入列表
    b = input("是否继续输入，n退出，任意键继续：")
    if b == 'n':
        break
#to_addr = input("请你输入收件邮箱：")
#发信服务器
smtp_server = 'smtp.qq.com'

text = '''
亲爱的朋友：
    我是洺洺，人生苦短，来跟我一起学习python吧
    洺洺
    2019.03.19
'''

#发信内容
msg = MIMEText(text,'plain','utf-8')
#邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(",".join(to_addrs))
msg['Subject'] = Header('打扰你了~')


# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)
#登录发信邮箱
server.login(from_addr, password) 
#发送邮件
server.sendmail(from_addr, to_addrs, msg.as_string()) 
#关闭服务器
server.quit()