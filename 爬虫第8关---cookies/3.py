import requests #引入requests模块
# 注意：此处需要先模拟发送验证码的请求，再模拟登录的请求。
# 请求验证码时，会返回一个json，json里会有validate_token。它在输入账号验证码模拟登录的时候，会用到。
session = requests.session() #创建会话
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
#添加请求头，避免被反爬虫
url = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
#登录的网址
tel = input('请输入手机号码：')
data = {
	'captcha_hash':'',
	'captcha_value':'',
	'mobile':tel,
	'scf':'ms',
}
#发送验证码的参数
token = session.post(url, headers=headers,data=data).json()['validate_token']
#在会话下，用post发起登录请求
print(token)

login_url = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
code = input('请输入验证码：')
login_data = {	
	'mobile':tel,
	'scf':"ms",
	'validate_code': code,
	'validate_token': token,
}
session.post(login_url, headers=headers, data=login_data)