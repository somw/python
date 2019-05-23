import scrapy
import bs4
from ..items import DoubanItem

# class DoubanSpider(scrapy.Spider):
#     name = 'douban'
#     allowed_domains = ['book.douban.com']
#     start_urls = ['https://book.douban.com/top250?start=0']

#     def parse(self,response):  #parse是解析
#         print(response.text)

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['book.douban.com']
    start_urls = []
    for x in range(3):
        url = 'https://book.douban.com/top250?start=' + str(x*25)
        start_urls.append(url)

    def parse(self, response): #parse是默认处理response的方法。
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        aa = bs.find_all('tr',class_ = 'item')
        for a in aa:
            item = DoubanItem() #实例化DoubanItem()这个类
            item['title'] = a.find_all('a')[1]['title']
            item['publish'] = a.find('p', class_ = 'pl').text
            item['nums'] = a.find('span', class_ = 'rating_nums').text
            print(['title','publish','nums'])
            yield item