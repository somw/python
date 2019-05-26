import scrapy,bs4,json
from ..items import ShopItem

class ShopSpider(scrapy.Spider):
    name = 'shop'
    allowed_domain = ['demo.dscmall.cn']
    ids= ['1105','1115','1129','1145','1160','347','463','630','547','1142','353','355','357','359','360','362','3','4','5','860']
    start_urls = []
    for x in range(20):
        url = 'https://demo.dscmall.cn/category.php?id='+ids[x]
        start_urls.append(url)

    def parse(self, response):
            soup =bs4.BeautifulSoup(response.text, 'html.parser')
            aa = soup.find_all('div', class_='gl-i-wrap')
            for a in aa:
                bb = a.find('div','p-img').find('a')['href']
                url1 = 'https://demo.dscmall.cn/{goods}'
                real_url = url1.format(goods=bb)
                yield scrapy.Request(real_url,callback=self.parse_shop)
    
    def parse_shop(self, response):
        item = ShopItem()
        datas = json.dumps(response.text, ensure_ascii= False, indent=4, separators=(',', ': '))
        resurl = json.loads(datas).encode('utf-8').decode('unicode_escape')
        item['gs_marktep'] =  datas['result_market'].replace('<em>¥</em>','') # 市场价
        item['gs_shopp'] =  resurl['original_shop_price'] # 本店价
        item['gs_num'] = resurl['attr_number'] # 库存量

        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        imgs = bs.find('div',class_='spec-items').find_all('li')
        for a in imgs:
            item['gs_img'] = a.find('a')['href'] # 图片路径
            item['thumb_img'] = a.find('img')['src']
            
        item['gs_brand'] = bs.find('div', class_='g-s-brand').find('img')['src'] # 品牌图片路径


        item['gs_dianpu'] = bs.findAll('dd',class_='column')[2].find('a').text # 店铺
        if bs.findAll('div',class_='crumbs-nav-item')[2] == '':
            item['gs_typeid'] = bs.findAll('div',class_='crumbs-nav-item')[1].find('span').text # 所属类型
        else:
            item['gs_typeid'] = bs.findAll('div',class_='crumbs-nav-item')[2].find('span').text

        item['gs_shopcateid'] = bs.findAll('div',class_='crumbs-nav-item')[0].find('span').text # 所属栏目
        item['gs_name'] = bs.findAll('dd',class_='column')[0].find('span').text # 商品标题
        item['gs_code'] = bs.findAll('dd',class_='column')[1].find('span').text[5:] # 商品编码
        item['gs_weight'] = bs.findAll('dd',class_='column')[3].find('span').text[3:] # 重量
        item['gs_time'] =  bs.findAll('dd',class_='column')[4].find('span').text[5:]  # 上架时间
        yield item

