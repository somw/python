import requests
url = 'https://www.ele.me/restapi/v2/pois?'
headers = { 'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' }
place = input('请输入你的收货地址：')
params = {
    'geohash': 'wwgq6gjzpq2g',
    'keyword': place,
    'limit': '20',
    'type': 'nearby'
}
address_res = requests.get(url, headers=headers, params=params)
#发起请求，将响应的结果赋值给res
address_json = address_res.json()
#用json()方法去解析response对象，并赋值给变量address_json

print('以下，是与'+place+'相关的位置信息：\n')