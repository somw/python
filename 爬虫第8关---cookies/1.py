import requests #引入requests模块
url = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
#把请求登录的网址赋值给url
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
#加请求头，为了模拟浏览器正常的访问，避免被反爬虫
data = {
    'log': 'spiderman',
    'pwd': 'crawler334566',
    'rememberme': 'forever',
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work',
    'testcookie': '1',
}
#把相关登录的参数封装成字典，赋值给data
login = requests.post(url, headers=headers, data=data)
#用requests.post发起请求，放入参数：请求登录的网址，请求头和参数，然后赋值给login
cookies = login.cookies
#提取cookies的方法：调用requests对象（login）的cookies属性获得登录的cookies,并赋值给变量cookies
#print(login)

url1 = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'
#我们想要评论的文章网址
data1 = {
    'comment': input('请输入你想要发表的评论：'),
    'submit': '发表评论',
    'comment_post_ID': '15',
    'comment_parent': '0',
}
#把相关评论的参数封装成字典，赋值给data1
comment = requests.post(url1, headers=headers, data=data1, cookies=cookies)
#用requests.post发起发表评论的请求，放入参数：文章网址，请求头、评论参数和cookies参数，然后赋值给comment
#调用cookies的方法就是在post请求中传入cookies=cookies的参数
print(comment.status_code)