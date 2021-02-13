# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime

class GemwholesalebotPipeline:
    def process_item(self, item, spider):
        if not self.stock_exist(item,spider):
            if(self.insert(item,spider)):
                print("Inserted New Record")
            else:
                print("Some Errors in my Website")
        else:
            print("Old Record No Need To add")
        return item
    def insert(self,item,spider):
        query = """INSERT INTO stocks (`title`, `image`, `image_url`, `cost_price`, `catalogue_value`, `sold_at`, `stock_list`, `new`,`parent_page`,stock_link, `created_at`, `updated_at`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)"""
        params = (
        item['title'], item['image'], item['image_url'], item['cost_price'], item['catalogue_value'], item['sold_at'],
        item['stock_list'], 1,item['parent_page'], item['stock_link'],datetime.now(), datetime.now())
        try:
            spider.cursor.execute(query, params)
            spider.connection.commit()
        except Exception as ex:
            spider.connection.rollback()
            return False
        return True
    def stock_exist(self,item,spider):
        query="""SELECT * FROM `stocks` WHERE `title`=%s"""
        params=(item['title'],)
        curs=spider.cursor
        res=False
        try:
            curs.execute(query, params)
            res= curs.with_rows
        except Exception as ex:
            spider.connection.rollback()
        print(res)
        return res


