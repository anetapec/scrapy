import pymongo
from tricity.items import HouseItem
from pymongo import MongoClient
import settings
from logging import log
import hashlib
import json

class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise HouseItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item
    
    for item in HouseItem():
            try:
                item = {item["price"]: item["url"]}
                result = hashlib.md5(json.dumps(item, sort_keys=True).encode('utf-8'))
                hash_value = result.hexdigest
                print(hash_value)
            except:
                print(" - ")
