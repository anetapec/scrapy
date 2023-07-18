import pymongo
from tricity import settings
from datetime import datetime
import hashlib
from scrapy.exporters import CsvItemExporter
from scrapy.exceptions import DropItem
from tricity.sendit_email import Mail



class MongoDBPipeline:

    def set_hash_url(self,item):
        result_url = hashlib.md5(f"{item['price']}{item['url']}".encode('utf-8'))
        hash_value_url = result_url.hexdigest()
        return hash_value_url
    
    def set_hash_area(self,item):
        result_area = hashlib.md5(f"{item['price']}{item['area']}".encode('utf-8'))
        hash_value_area = result_area.hexdigest()
        return hash_value_area

    def set_scrapping_date(self):
        now = self.time_now.strftime('%Y-%m-%d %H:%M:%S')
        return now
    
    def set_name_file(self, spider_mongo_collection):
        file_timestamp = self.time_now.strftime('%Y-%m-%d_%H-%M-%S')
        self.filename = str(f"{spider_mongo_collection}_{file_timestamp}.csv") 
   
    def open_spider(self, spider):
        self.time_now = datetime.now()
        spider_mongo_collection = spider.custom_settings["collection"]
        self.scrapping_date = self.set_scrapping_date()
        self.client = pymongo.MongoClient(settings.mongodb_uri)
        db = self.client[settings.mongodb_db]
        self.collection = db[spider_mongo_collection]
        self.set_name_file(spider_mongo_collection=spider.custom_settings["collection"])
        self.csv_file = open(self.filename, 'w+b')
        self.exporter = CsvItemExporter(self.csv_file)
        self.exporter.start_exporting() 
        


    def close_spider(self, spider):
        self.client.close()
        self.exporter.finish_exporting()
        self.csv_file.close()
        mail = Mail(self.filename)
        mail.send()




        # contents = self.csv_file.read()
        # if contents == b'':
            # self.csv_file.close()

        # else:
            # self.csv_file.close()
            # mail = Mail(self.filename)
            # mail.send()
###############################
        # contents = len(self.filename)
        # if contents == 0: 
            # self.csv_file.close()
            
            
        # else:      
            # self.csv_file.close()
            # mail = Mail(self.filename)
            # mail.send()
        
        

    def process_item(self, item, spider):
        item['price_per_meter'] = (round(float(item['price']) / float(item['area']), 2))
        item['last_seen_date'] = self.scrapping_date
        item['hash'] = self.set_hash_url(item)
        item['hash_area'] = self.set_hash_area(item)
        filter_or = { '$or': [ {'hash_area': item['hash_area']}, {'hash': item['hash']} ] }
        
        if (item['price_per_meter'] < 300 ):
             raise DropItem(f"Advertisement for a house for rent ")
        
        if self.collection.count_documents((filter_or), limit = 1) !=0 :
            new_value = { '$set': {'last_seen_date': item['last_seen_date']}}
            self.collection.update_one(filter_or, new_value)
            raise DropItem(f"Duplicate item found: { item['url']} ")
        
        else:
            item['scrapping_date'] = self.scrapping_date
            data = dict(item)
            self.collection.insert_one(data)
            self.exporter.export_item(item)

        return item
    












        

        
