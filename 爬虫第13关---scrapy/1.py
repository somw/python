import scrapy
class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    publish = scrapy.Field()
    score = scrapy.Field()

book = DoubanItem() #实例化一个DoubanItem对象
book['title'] = 'abc'
book['publish'] = 'abcccc'
book['score'] = '8.1'

print(book)
print(type(book))