import pymongo
from tricity import settings
from datetime import datetime
import hashlib
import os

 
class MongoDBPipeline:
    
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
        mongo_uri = os.getenv('MONGO_URI',settings.mongodb_uri)
        self.client = pymongo.MongoClient(mongo_uri)
        db = self.client[settings.mongodb_db]
        self.collection = db[spider_mongo_collection]

    def close_spider(self, spider):
        self.client.close()

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
            
        
        return item