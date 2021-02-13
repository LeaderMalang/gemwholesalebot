import scrapy


class GemwholesaleSpider(scrapy.Spider):
    name = 'gemwholesale'
    allowed_domains = ['gemwholesale.co.uk']
    start_urls = ['https://www.gemwholesale.co.uk/acatalog/Customer-Returns.html']

    def parse(self, response):
        productContainer=response.xpath('//div[@class="product-details"]')
        for product in productContainer:
            print(product)
            title=product.xpath('//div[@class="product-details"]/div/table/a[2]/h2/text()').get()
            image=product.css(".product-image").xpath('//p/a/img/@src').get()
            cost_price=product.xpath('table[1]/tr[3]/td[2]/p/prices/div/span/span/text()').get()
            catalogue_value=product.xpath('table[1]/tr[1]/td[2]/span/text()').get()
            sold_at=product.xpath('table[1]/tr[2]/td[2]/span/text()').get()
            stock_list=product.css('.product-text a::attr(href)').get()
            print(title,image,cost_price,catalogue_value,sold_at,stock_list)

        print(response)
