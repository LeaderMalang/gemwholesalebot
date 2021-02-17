# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GemwholesalebotItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    image=scrapy.Field()
    image_urls=scrapy.Field()
    cost_price=scrapy.Field()
    catalogue_value=scrapy.Field()
    sold_at=scrapy.Field()
    stock_list=scrapy.Field()
    parent_page=scrapy.Field()
    stock_link=scrapy.Field()

