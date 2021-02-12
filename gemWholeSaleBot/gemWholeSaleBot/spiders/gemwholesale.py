import scrapy


class GemwholesaleSpider(scrapy.Spider):
    name = 'gemwholesale'
    allowed_domains = ['gemwholesale.co.uk']
    start_urls = ['https://www.gemwholesale.co.uk/acatalog/Customer-Returns.html']

    def parse(self, response):
        productContainer=response.xpath('//div[@class="product-details"]').getall()
        for product in productContainer:
            title=product.xpath('//a[@target="ActPopup"]/h2::text()').get()
            image=product.xpath('//p[@class="product-image"]/a/img/@src').get()
            cost_price=product.xpath('//span[@class="product-price"]/span::text()').get()
            catalogue_value=product.xpath("//table[@id='stockdetails']/tbody/tr[1]/td[2]/span::text()").get()

        print(response)
