import scrapy


class GemwholesaleSpider(scrapy.Spider):
    name = 'gemwholesale'
    allowed_domains = ['gemwholesale.co.uk']
    start_urls = ['https://gemwholesale.co.uk/']

    def parse(self, response):
        pass
