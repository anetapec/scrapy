import pymongo
import sys
from .items import HouseItem
import tricity.settings

class MongoDBPipeline:

    
    #MONGO_URI = 'mongodb://127.0.0.1:27017/'

    def __init__(self, mongodb_uri, mongodb_db, collection_name):
        self.mongodb_uri = mongodb_uri
        self.mongodb_db = mongodb_db
        self.collection_name = collection_name
        if not self.mongodb_uri: sys.exit("You need to provide a Connection String.")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_uri=crawler.settings.get('mongodb_uri'),
            mongodb_db=crawler.settings.get('mongodb_db', 'item'),
            collection_name = crawler.settings.get('collection_name', 'item')
        )

    def open_spider(self, spider):
        self.client = self.mongodb_uri
        self.db = self.client[self.mongodb_db]
        self.collection_name = self.mongodb_uri[self.mongodb_db]
        # Start with a clean database
        self.db[self.collection_name].delete_many({})

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = dict(HouseItem(item))
        self.db[self.collection_name].insert_one(data)
        return item