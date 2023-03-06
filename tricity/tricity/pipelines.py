import pymongo
#from .items import HouseItem
from tricity import settings
from datetime import datetime

class MongoDBPipeline:

    def open_spider(self, spider):
        connection = pymongo.MongoClient(settings.mongodb_uri)
        db = connection[settings.mongodb_db]
        self.client = pymongo.MongoClient(settings.mongodb_uri)
        self.collection = db[settings.colection_name]
        #start with a clean database
        self.collection.delete_many({})

    def close_spider(self, spider):
        self.client.close()
    
    @property
    def date_scraping(self):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return now
    
    def proces_item(self, item, spider):
        item['date'] = self.date_scraping
        data = dict(item)
        self.collection.insert_one(data)
    
        return item
    
      
        
    
   
   
    