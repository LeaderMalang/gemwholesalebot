import scrapy
import mysql.connector


class GemwholesaleSpider(scrapy.Spider):
    name = 'gemwholesale'
    allowed_domains = ['gemwholesale.co.uk']
    start_urls = [
        'https://www.gemwholesale.co.uk/acatalog/Customer-Returns.html',
        'https://www.gemwholesale.co.uk/acatalog/Clearance.html',
        'https://www.gemwholesale.co.uk/acatalog/Small-Electrical.html',
        'https://www.gemwholesale.co.uk/acatalog/Electrical-Clearance-Stock.html',
        'https://www.gemwholesale.co.uk/acatalog/Grade-1-Clothing.html',
        'https://www.gemwholesale.co.uk/acatalog/Clothing-Clearance.html',
        'https://www.gemwholesale.co.uk/acatalog/Watches-Clearance.html',
        'https://www.gemwholesale.co.uk/acatalog/Watches-Customer-Returns.html',
        'https://www.gemwholesale.co.uk/acatalog/Jewellery-Clearance-Stock.html',
        'https://www.gemwholesale.co.uk/acatalog/Jewellery-Customer-Returns.html',
        'https://www.gemwholesale.co.uk/acatalog/Toys-Customer-Returns.html'
    ]

    host = 'localhost'
    user = 'root'
    password = ''
    db = 'gembot'

    def __init__(self):
        self.connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.db, use_unicode=True,
                                          charset="utf8")
        self.cursor = self.connection.cursor()

    def insert(self, query, params):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except Exception as ex:
            self.connection.rollback()

    def __del__(self):
        self.connection.close()
    def parse(self, response):
        items=dict()
        productContainer=response.xpath('//div[@class="product-details"]')
        print('stock len',len(productContainer),response.request.url)
        for product in productContainer:

            title=product.xpath('//div[@class="product-details"]/div/table/a[2]/h2/text()').get()
            if title is None:
                continue
            image=product.css(".product-image").xpath('//p/a/img/@src').get()
            cost_price=product.xpath('table[1]/tr[3]/td[2]/p/prices/div/span/span/text()').get()
            catalogue_value=product.xpath('table[1]/tr[1]/td[2]/span/text()').get()
            sold_at=product.xpath('table[1]/tr[2]/td[2]/span/text()').get()
            stock_list=product.css('.product-text > a::attr(href)').get()
            info=product.xpath('//div[@class="product-details"]/div/table/a[2]/@href').get()
            image_url="https://www.gemwholesale.co.uk/acatalog/"+image
            stock_link="https://www.gemwholesale.co.uk/acatalog/"+info
            #print(title,image,cost_price,catalogue_value,sold_at,stock_list)

            items.update({
                'title': title,
                'image': image,
                'image_urls': [image_url],
                'cost_price': cost_price,
                'catalogue_value': catalogue_value,
                'sold_at': sold_at,
                'stock_list': stock_list,
                'parent_page': response.request.url,
                "stock_link":stock_link
            })


            yield items


