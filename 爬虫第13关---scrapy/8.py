import requests
url = 'https://mp.weixin.qq.com/mp/appmsgreport?action=page_time_5s&__biz=MzI5MzU5NDIzNw==&uin=&key=&pass_ticket=&wxtoken=777&devicetype=&clientversion=&appmsg_token=&x5=0&f=json'

params = {
    'action': 'page_time_5s',
    '__biz': 'MzI5MzU5NDIzNw==',
    'uin': '',
    'key': '',
    'pass_ticket': '',
    'wxtoken': '777',
    'devicetype': '',
    'clientversion': '',
    'appmsg_token': '',
    'x5': '0',
    'f': 'json',
    'publish_time': '1555980199'
}
res = requests.get(url,params=params)
json_res = res.json()
print(json_res)