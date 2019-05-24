# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import openpyxl
class JobuiPipeline(object):
    def __init__(self): # 初始化函数，当类实例化时这个方法会自启动
        self.wb = openpyxl.Workbook() #创建工作簿
        self.ws = self.wb.active # 定位活动表
        self.ws.append(['公司','职位','地址','招聘信息'])

    def process_item(self, item, spider):
        line = [item['company'],item['position'],item['address'],item['detail']]
        self.ws.append(line)
        return item
    
    def close_spider(self, spider):
        self.wb.save('./jobui.xlsx')
        self.wb.close()
