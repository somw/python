import scrapy,bs4
from ..items import JobuiItem

class JobuiSpider(scrapy.Spider):
    name = 'jobui'
    allowed_domains = ['www.jobui.com']
    start_urls = ['https://www.jobui.com/rank/company/']

    def parse(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        aa = bs.find_all('ul', class_ = 'textList flsty cfix')
        for x in aa:
            a_list = x.find_all('a')
            for y in a_list:
                company_id = y['href']
                url = 'https://www.jobui.com{id}jobs/'
                real_url = url.format(id=company_id)
                yield scrapy.Request(real_url, callback=self.parse_job)
    
    def parse_job(self, response):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        company = bs.find('h1',id='companyH1').text.strip()
        cc = bs.find_all('div', class_='job-simple-content')
        for a in cc:
            item = JobuiItem()
            item['company'] = company
            item['position'] = a.find('div', class_='job-segmetation').find('h3').text
            spanall = a.find('div', class_='job-desc').findAll('span')
            item['address'] = spanall[0].text
            item['detail'] = spanall[1].text
            yield item