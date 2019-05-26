# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShopItem(scrapy.Item):
    # define the fields for your item here like:
    gs_name = scrapy.Field() # 商品标题
    gs_code = scrapy.Field() # 商品编码
    gs_img = scrapy.Field() # 图片路径
    thumb_img = scrapy.Field() # 缩略图
    gs_marktep = scrapy.Field()  # 市场价
    gs_shopp = scrapy.Field()  # 本店价
    gs_shopcateid = scrapy.Field() # 所属栏目
    gs_dianpu = scrapy.Field() # 店铺
    gs_brand = scrapy.Field() # 品牌图片路径
    gs_typeid = scrapy.Field() # 所属类型
    gs_weight = scrapy.Field() # 重量
    gs_num = scrapy.Field() # 库存量
    gs_time = scrapy.Field() # 上架时间