# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeibospiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    content = scrapy.Field()
    postTime = scrapy.Field()
    image = scrapy.Field()
    outLink = scrapy.Field()
    subUser = scrapy.Field()
    subContent = scrapy.Field()
    reOutLink = scrapy.Field()
    subTime = scrapy.Field()
    reImage = scrapy.Field()
    pass


