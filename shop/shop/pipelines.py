# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import openpyxl
class ShopPipeline(object):
    def __init__(self): # 初始化函数，当类实例化时这个方法会自启动
        self.wb = openpyxl.Workbook() #创建工作簿
        self.ws = self.wb.active # 定位活动表
        self.ws.append(['商品标题','商品编码','重量','上架时间','所属栏目','所属类型','店铺','原图','缩略图','品牌图片','描述'])

    def process_item(self, item, spider):
        line = [item['gs_name'],item['gs_code'],item['gs_weight'],item['gs_time'],item['gs_shopcateid'],item['gs_typeid'],item['gs_dianpu'],item['gs_img'],item['thumb_img'],item['gs_brand'],item['gs_dec']]
        self.ws.append(line)
        return item

    def close_spider(self, spider):
        self.wb.save('./shop.xlsx')
        self.wb.close()
