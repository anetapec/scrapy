import pymongo
from .items import HouseItem
from tricity import settings
class MongoDBPipeline:

    def open_spider(self, spider):
        connection =  pymongo.MongoClient(settings.mongodb_uri)
        db = connection[settings.mongodb_db]
        self.collection = db[settings.collection_name]
        # Start with a clean database
        self.collection.delete_many({})

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = dict(item)
        self.collection.insert_one(data)
        return item