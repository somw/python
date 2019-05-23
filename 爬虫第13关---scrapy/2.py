import scrapy
import bs4

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250?start=0']

    def parse(self,response):  #parse是解析
        print(response.text)

url = DoubanSpider()
print(url)