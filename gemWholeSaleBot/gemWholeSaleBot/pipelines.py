# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
from scrapy.pipelines.images import ImagesPipeline
import pdfkit
import requests
import telegram

class GemwholesalebotPipeline:
    def process_item(self, item, spider):
        if not self.stock_exist(item,spider):
            if(self.insert(item,spider)):
                print("Inserted New Record")
                # endpoint="http://109.228.60.191:5000/send_message?title="+item['title']+"&stock_list="+item['stock_list']
                # response=requests.get(endpoint) response
                print("Sending new listing and stock list")
            else:
                print("Some Errors in my Website")
        else:
            print("Old Record No Need To add")
        return item

    # def send_message(self,message,stock_list):
    #     bot_token = '1598350721:AAFA4YMJBqxeVfzIjfMzqbP3PMtsMZSvdsk'
    #     bot_chatID = '1644262765'
    #     bot_message = message
    #     stocklistLink = stock_list
    #     url = 'img/stock_list/'+bot_message+'.pdf'
    #     pdfkit.from_url(stocklistLink, url)
    #     bot = telegram.Bot(token=bot_token)
    #     bot.sendMessage(chat_id=bot_chatID, text=bot_message)
    #     bot.sendDocument(chat_id=bot_chatID, document=open(url, 'rb'))
    #     print("Sending new listing and stock list")
    def insert(self,item,spider):
        query = """INSERT INTO stocks 
        (`title`, `image`, `image_url`, `cost_price`, `catalogue_value`, `sold_at`, `stock_list`, `new`,`parent_page`,stock_link, `created_at`, `updated_at`) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE image = %s;
        """
        params = (
        item['title'], item['image'], item['image_urls'][0], item['cost_price'], item['catalogue_value'], item['sold_at'],
        item['stock_list'], 1,item['parent_page'], item['stock_link'],datetime.now(), datetime.now(),item['image'])
        try:
            spider.cursor.execute(query, params)
            spider.connection.commit()
        except Exception as ex:
            spider.connection.rollback()
            return False
        return True
    def stock_exist(self,item,spider):
        query="""SELECT * FROM `stocks` WHERE `image`=%s"""
        params=(item['image'],)
        curs=spider.cursor
        res=False
        try:
            curs.execute(query, params)
            res= curs.with_rows
        except Exception as ex:
            spider.connection.rollback()
        print(res)
        return res
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_urls'])
# class GemImagebot(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         yield scrapy.Request(item['image_urls'])
#
#     def item_completed(self, results, item, info):
#         results['path']
#         if not image_paths:
#             raise DropItem("Item contains no images")
#         item['image'] = results['path']
#         return item
#
#
