# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Sc01Item(scrapy.Item):
    raceid = scrapy.Field()
    racetitle = scrapy.Field()

    place = scrapy.Field()
    postnum = scrapy.Field()
    horsenum = scrapy.Field()
    horsename = scrapy.Field()
    sex = scrapy.Field()
    age = scrapy.Field()
    weight = scrapy.Field()
    jockey = scrapy.Field()
    time = scrapy.Field()
    margin  = scrapy.Field()
    position = scrapy.Field()
    last3f = scrapy.Field()
    odds = scrapy.Field()
    fav = scrapy.Field()
    horseweight = scrapy.Field()
    horseweightdiff = scrapy.Field()
    trainer = scrapy.Field()
    owner = scrapy.Field()
    addedmoney = scrapy.Field()
    tmp01 = scrapy.Field()