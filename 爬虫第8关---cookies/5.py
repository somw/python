import requests,json
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
english = input('请输入要翻译的文字：')
data = {
	'i':english,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'15623116908171',
    'sign':'d72fb820959fdcd6c80f8fc0ec68cbfb',
    'ts':'1562311690817',
    'bv':'530358e1f56d925c582f7d2d49f07756',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME'
}
res = requests.post(url,data)
res_json =json.loads(res.text)
print('翻译的结果：' + res_json['translateResult'][0][0]['tgt'])

