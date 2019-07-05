import requests
session = requests.session()
#print(session)

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


address_url = 'https://www.ele.me/restapi/v2/pois?'
headers = { 'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' }
place = input('请输入你的收货地址：')
params = {
    'geohash': 'wwgq6gjzpq2g',
    'keyword': place,
    'limit': '20',
    'type': 'nearby'
}
address_res = requests.get(address_url, headers=headers, params=params)
#发起请求，将响应的结果赋值给res
address_json = address_res.json()
#用json()方法去解析response对象，并赋值给变量address_json
print(address_json)
print('以下，是与'+place+'相关的位置信息：\n')
n=0
for address in address_json:
   print(str(n) + '.' + address['name'] + ':' + address['short_address'])
   n = n + 1

address_num = int(input('请输入你选择位置的序号：'))
final_address = address_json[address_num]
print(final_address)

restaurants_url = 'https://www.ele.me/restapi/shopping/restaurants?'
# 使用带有餐馆列表的那个XHR地址
params = {
    'extras[]': 'activities',
    'geohash': final_address['geohash'],
    'latitude': final_address['latitude'],
    'limit': '24',
    'longitude': final_address['longitude'],
    'offset': '0',
    'terminal': 'web',
}
# 将参数封装，其中geohash和经纬度，来自前面获取到的数据

restaurants_res = session.get(restaurants_url,params=params)
# 发起请求，将响应的结果，赋值给restaurants_res
restaurants = restaurants_res.json()
# 把response对象，转为json
# print(restaurants)
for restaurant in restaurants:
# restaurants最外层是一个列表，它可被遍历。restaurant则是遍历，里面包含了单个餐厅的所有信息
    print(restaurant['id'] + ',' + restaurant['name'])