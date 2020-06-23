# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SephoraItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	brand_name = scrapy.Field()
	product = scrapy.Field()
	p_id = scrapy.Field()
	p_price = scrapy.Field()
	p_shade = scrapy.Field()
	
	pass
