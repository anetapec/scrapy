import pymongo
from tricity import settings
from datetime import datetime
import hashlib

 
class MongoDBPipeline:
    
    def set_hash(self,item):
        result = hashlib.md5(f"{item['price']}{item['url']}".encode('utf-8'))
        hash_value = result.hexdigest()
        return hash_value

    def set_scrapping_date(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return now

    def open_spider(self, spider):
        self.scrapping_date = self.set_scrapping_date()
        self.client = pymongo.MongoClient(settings.mongodb_uri)
        db = self.client[settings.mongodb_db]
        self.collection = db[settings.colection_name]
        
        #start with a clean database
        self.collection.delete_many({})

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        item['price_per_meter'] = str(round(float(item['price']) / float(item['area']), 2))
        item['hash'] = self.set_hash(item)
        item['scrapping_date'] = self.scrapping_date
        data = dict(item)
        filter_dict = {'hash': self.set_hash}
        if self.collection.find(filter_dict).limit(1).explain():
            #if not item['hash'] in data:
            self.collection.insert_one(data)
        else:
            item['last_seen_date'] = self.scrapping_date
            self.collection.update_one(data)
            data = dict(item)
        return item