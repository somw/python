import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.qq.com'
from_addr = 'sompt@qq.com'
to_addr = 'somw@qq.com'
msg = MIMEText('hello,I am mingming. good afternoon!','plain','utf-8')

server = smtplib.SMTP(smtp_server)
server.connect(smtp_server, 25)
server.login(from_addr, 'lussksqqjrxyca') 
server.sendmail(from_addr, to_addr, msg.as_string()) 
server.quit()