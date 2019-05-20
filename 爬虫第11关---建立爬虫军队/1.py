import requests,time
start = time.time()
url_list = ['https://www.baidu.com/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']
for url in url_list:
    r = requests.get(url)
    print(url, r.status_code)
end = time.time()
print(end-start)