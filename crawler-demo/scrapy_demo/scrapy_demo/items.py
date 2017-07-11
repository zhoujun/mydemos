# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Item, Field

class WeixinItem(Item):
    title = Field()
    link = Field()
    des = Field()

class WoaiduItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    book_name = Field()
    author = Field()
    original_url = Field()

class ItjuziItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    company_name = Field()
    cat1 = Field()
    cat2 = Field()
    created_date = Field()
    addr = Field()
    status = Field()
