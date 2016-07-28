# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CoursesItem(scrapy.Item):
    # define the fields for your item here like:
    course = scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    phone_number = scrapy.Field()
    par = scrapy.Field()
    handicap = scrapy.Field()
    colors = scrapy.Field()
    #score_card = scrapy.Field()