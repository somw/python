import smtplib
from email.mime.text import MIMEText
from email.header import Header

mailhost='smtp.qq.com'
#把QQ邮箱的服务器地址赋值到变量mailhost,地址应为字符串格式
qqmail = smtplib.SMTP()
#实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的属性和方法了
qqmail.connect(mailhost,25)
#连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。

account = input('请输入你的电子邮箱：')
password = input('请输入你的密码：')
 #请输入你的密码：oapjxyjhifrqbej
qqmail.login(account,password)

receiver = input('请输入收件人的电子邮箱：')
# list_all = '13354'

content = '亲爱的，本周的热门热菜如下'
message = MIMEText(content,'plain','utf-8')
subject = '周末吃什么'
message['Subject'] = Header(subject,'utf-8')

try:
    qqmail.sendmail(account, receiver, message.as_string())
    print('邮件发送成功')
except:
    print('邮件发送失败')
qqmail.quit()