import pymongo
#from .items import HouseItem
from tricity import settings
from datetime import datetime
 
class MongoDBPipeline:

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
        item['scrapping_date'] = self.scrapping_date
        data = dict(item)
        self.collection.insert_one(data)
        return item