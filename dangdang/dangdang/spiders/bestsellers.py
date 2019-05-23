import scrapy
import bs4
from ..items import DangdangItem

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domain = ['http://bang.dangdang.com']
    start_urls = []
    for i in range(3):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-' + str(i+1)
        start_urls.append(url)
    
    def parse(self, response): #parse是默认处理response的方法
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        aa = bs.find('ul', class_ = 'bang_list_mode').find_all('li')
        for a in aa:
            item = DangdangItem()
            item['name'] = a.find('div', class_ = 'name').find('a')['title']
            item['anower'] = a.find('div', class_ = 'publisher_info').find('a')['title']
            item['price'] = a.find('div', class_ = 'price').find('p').find('span', class_ = 'price_n').text
            print(['name','anower','price'])
            yield item
