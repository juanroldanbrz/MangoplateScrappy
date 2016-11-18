# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Restaurant(scrapy.Item):
    name = scrapy.Field()
    addressLocality = scrapy.Field()
    telephone = scrapy.Field()
    cuisineType = scrapy.Field()
    priceRange = scrapy.Field()
    openingHours = scrapy.Field()