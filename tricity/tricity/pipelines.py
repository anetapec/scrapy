import pymongo
from tricity import settings
from datetime import datetime
import hashlib
from scrapy.exporters import CsvItemExporter
import csv


class MongoDBPipeline:

    #custom_settings = {
    #'FEEDS': {'scraping_data_csv': {'format': 'csv',}}
#}



    def set_hash(self,item):
        result = hashlib.md5(f"{item['price']}{item['url']}".encode('utf-8'))
        hash_value = result.hexdigest()
        return hash_value

    def set_scrapping_date(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return now

    

    def open_spider(self, spider):
        spider_mongo_collection = spider.custom_settings["collection"]
        self.scrapping_date = self.set_scrapping_date()
        self.client = pymongo.MongoClient(settings.mongodb_uri)
        db = self.client[settings.mongodb_db]
        self.collection = db[spider_mongo_collection]





    def close_spider(self, spider):
        self.client.close()

        # self.csv_file = open('scraping_data_csv', 'wb')
        # self.csv_exporter = CsvItemExporter(self.csv_file)

        #self.csv_exporter.fields_to_export = ['price', 'url', 'area', 'price_per_meter', 'scrapping_date']
        # self.csv_exporter.start_exporting()

        # self.csv_exporter.finish_exporting()

        # self.csv_file.close()





    def process_item(self, item, spider):
        item['price_per_meter'] = (round(float(item['price']) / float(item['area']), 2))
        item['last_seen_date'] = self.scrapping_date
        item['hash'] = self.set_hash(item)
        filter_dict = {'hash': item['hash']}
        if self.collection.count_documents((filter_dict), limit = 1) !=0:
            new_value = { '$set': {'last_seen_date': item['last_seen_date']}}
            self.collection.update_one(filter_dict, new_value)
        else:
            item['scrapping_date'] = self.scrapping_date
            data = dict(item)
            self.collection.insert_one(data)
            
            if item['scrapping_date'] == self.set_scrapping_date():

                with open('scraping_data_csv', mode='w') as csv_file:
                    writer = csv.writer(csv_file)
                    scraped_data = self.collection.insert_one(data)
                    writer.writerow(scraped_data)
                    





            #self.csv_exporter.export_item(item)


        return item
    
# class MyCustomFilter:

    # def __init__(self, feed_options):
        # self.feed_options = feed_options

    # def accepts(self, item):
        # if "scrapping_date" in item and item["scrapping_date"] == MongoDBPipeline.set_scrapping_date():
            # return True
        # return False
    
    