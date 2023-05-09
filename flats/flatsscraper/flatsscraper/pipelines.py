''''
import pymongo
from flatsscraper import settings
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

    def close_spider(self, spider):
        self.client.close()

'''    

from itemadapter import ItemAdapter


class FlatsscraperPipeline:
    
    def __init__(self):
        pass

    def process_item(self, item, spider):

        
        return item
