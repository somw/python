import requests #引入requests模块
# 注意：此处需要先模拟发送验证码的请求，再模拟登录的请求。
# 请求验证码时，会返回一个json，json里会有validate_token。它在输入账号验证码模拟登录的时候，会用到。
session = requests.session() #创建会话
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
#添加请求头，避免被反爬虫
url = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
#登录的网址
data = {
	'mobile': '18522268833',
	'scf': 'ms',
	'validate_code': '"177326"',
	'validate_token': '"20678afa382d726e8a4fd50258734752ba53bfff9e542a9f7feb4ad4f46d8689"',
}
#登录的参数
login = session.post(url, headers=headers,data=data)
#在会话下，用post发起登录请求
cookies = login.cookies 
print(login)