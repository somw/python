import requests
from bs4 import BeautifulSoup

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

url3 = 'https://demo.dscmall.cn/goods.php?act=price&id=843'
params = {
    'act': 'price',
    'id': '843',
    'attr': '',
    'number': '1',
    'warehouse_id': '2',
    'area_id': '19',
    'onload': 'onload',
    '1558809852328328': ''
}
res_price = requests.get(url3,headers=headers,params=params)
resurl = res_price.json()
gs_marktep =  resurl['result_market'].replace('<em>¥</em>','') # 市场价
gs_shopp =  resurl['original_shop_price'] # 本店价
gs_num = resurl['attr_number'] # 库存量


url2 = 'https://demo.dscmall.cn/goods.php?id=843'
res1 = requests.get(url2,headers=headers)
soup1 = BeautifulSoup(res1.text,'html.parser')

imgs = soup1.find('div',class_='spec-items').find_all('li')
for a in imgs:
    gs_img = a.find('a')['href'] # 图片路径
    thumb_img = a.find('img')['src']
    
gs_brand = soup1.find('div', class_='g-s-brand').find('img')['src'] # 品牌图片路径


gs_dianpu = soup1.findAll('dd',class_='column')[2].find('a').text # 店铺
if soup1.findAll('div',class_='crumbs-nav-item')[2] == '':
    gs_typeid = soup1.findAll('div',class_='crumbs-nav-item')[1].find('span').text # 所属类型
else:
    gs_typeid = soup1.findAll('div',class_='crumbs-nav-item')[2].find('span').text

gs_shopcateid = soup1.findAll('div',class_='crumbs-nav-item')[0].find('span').text # 所属栏目
gs_name = soup1.findAll('dd',class_='column')[0].find('span').text # 商品标题
gs_code = soup1.findAll('dd',class_='column')[1].find('span').text[5:] # 商品编码
gs_weight = soup1.findAll('dd',class_='column')[3].find('span').text[3:] # 重量
gs_time =  soup1.findAll('dd',class_='column')[4].find('span').text[5:]  # 上架时间