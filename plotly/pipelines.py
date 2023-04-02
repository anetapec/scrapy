import pymongo
import pandas as pd
from datetime import datetime

def load_collection(self):
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client['tricity']
    collection = db['houses']
    df = pd.DataFrame(list(collection.find()))
    return df

def count_avg_price(self):
    avg_price = self.collection.aggregate([{
        '$group': {
            '_id': 'hash',
            'avg_price': {'$avg': '$price_per_meter'}
        }}])
    for x in avg_price:
        return(x)

def count_houses_exposed(self):
    number_houses_exposed = collection.aggregate([{'$match': {'last_seen_date': '2023-04-02 20:22:57'}}, {'$count': 'houses_exposed'}])
    for dokument in number_houses_exposed:
        return(dokument)
    
def count_houses_sold(self):
    houses_sold = collection.aggregate([{'$match': {'last_seen_date': {'$ne': '2023-04-02 20:22:57'}}}, {'$count': 'houses_sold'}])
    for h_sold in houses_sold:
        return(h_sold)
    
