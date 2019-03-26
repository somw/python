import requests
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
res.encoding = 'utf-8'
aa = res.text
aaa = open('aaa.txt','a+')
aaa.write(aa)
aaa.close()