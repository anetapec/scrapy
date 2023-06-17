import pymongo
import settings
from datetime import datetime
import hashlib
from scrapy.exporters import CsvItemExporter
import csv
from scrapy.exceptions import DropItem
import os


class MongoDBPipeline:

    # custom_settings = {
#    # 'FEEDS': {'/scraping_data_csv/%(name)s_%(time)s.csv': {'format': 'csv',}}
#}



    def set_hash_url(self,item):
        result_url = hashlib.md5(f"{item['price']}{item['url']}".encode('utf-8'))
        hash_value_url = result_url.hexdigest()
        return hash_value_url
    
    def set_hash_area(self,item):
        result_area = hashlib.md5(f"{item['price']}{item['area']}".encode('utf-8'))
        hash_value_area = result_area.hexdigest()
        return hash_value_area

    def set_scrapping_date(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return now

    

    def open_spider(self, spider):
        spider_mongo_collection = spider.custom_settings["collection"]
        self.scrapping_date = self.set_scrapping_date()
        self.client = pymongo.MongoClient(settings.mongodb_uri)
        db = self.client[settings.mongodb_db]
        self.collection = db[spider_mongo_collection]
        filename = str(spider_mongo_collection + self.set_scrapping_date())
        file = open(filename + ".csv", 'w+b')   
        self.exporter = CsvItemExporter(file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.client.close()
        self.exporter.finish_exporting()
        self.file.close()


    def process_item(self, item, spider):
        item['price_per_meter'] = (round(float(item['price']) / float(item['area']), 2))
        item['last_seen_date'] = self.scrapping_date
        item['hash'] = self.set_hash_url(item)
        item['hash_area'] = self.set_hash_area(item)
        filter_dict = {'hash': item['hash']}
        filter_dict_area = {'hash_area': item['hash_area']}
        if self.collection.count_documents((filter_dict), limit = 1) !=0 :
            new_value = { '$set': {'last_seen_date': item['last_seen_date']}}
            self.collection.update_one(filter_dict, new_value)
            raise DropItem("Duplicate item found: {}".format(item['scrapping_date']))
        if self.collection.count_documents((filter_dict_area), limit = 1) !=0 :
            new_value = { '$set': {'last_seen_date': item['last_seen_date']}}
            self.collection.update_one(filter_dict_area, new_value)
            raise DropItem("Duplicate item found: {}".format(item['scrapping_date']))
        else:
            item['scrapping_date'] = self.scrapping_date
            data = dict(item)
            self.collection.insert_one(data)
            
            self.exporter.export_item(item)

        return item
    
    