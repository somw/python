import scrapy,bs4
from ..items import DoubandpItem

class DoubandpSpider(scrapy.Spider):
    name = 'doubandp'
    allowed_domain = ['book.douban.com']
    start_urls = []
    for a in range(2):
        url = 'https://book.douban.com/top250?start='+ str(a *25)
        start_urls.append(url)

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        aa = bs.find('div', class_ = 'indent').find_all('div', class_= 'pl2')
        for x in aa:
            cc = x.find('a')['href']
            url1 = '{id}comments/'
            real_url1 = url1.format(id=cc)
            yield scrapy.Request(real_url1,callback=self.parse_douban)
    
    def parse_douban(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        bookname = bs.find('div', id='wrapper').text.split()[0]
        dd = bs.find_all('div',class_='comment')
        for b in dd:
            item = DoubandpItem()
            item['bookname'] = bookname
            item['plid'] = b.find_all('a')[1].text
            item['dpcontent'] = b.find('span',class_='short').text
            yield item
