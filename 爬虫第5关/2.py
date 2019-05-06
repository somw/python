import requests
#引用requests模块
url = "https://www.kuaidi100.com/query"
numpostid = input("你的快递单号是什么？")
nametype = input("你的快递是什么物流？")
params = {
    'type': nametype,
	'postid': numpostid,
	'temp': '0.3885539020692925',
	'phone': '',
}
#将参数封装为字典
res_kuaidi = requests.get(url,params=params)
#调用get方法，下载这个字典
resurl = res_kuaidi.json()
#调用json方法，将response对象，转为列表/字典
print('最新物流状态：'+ resurl['data'][0]['context'])
#以context为键，查找最新物流状态信息