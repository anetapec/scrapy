import pymongo
import pandas as pd
from datetime import datetime

def load_collection(self):
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client['tricity']
    collection = db['houses']
    df = pd.DataFrame(list(collection.find()))
    return df

def count_avg_price_per_meter(self):
    avg_price = self.collection.aggregate([{
        '$group': {
            '_id': 'hash',
            'avg_price': {'$avg': '$price_per_meter'}
        }}])
    for x in avg_price:
        return(x)
    
def count_median_price_per_meter(self):
    median_price_per_meter = self.df['price_per_meter'].median()
    return median_price_per_meter
    
def count_avg_price(self):
    avg_price = self.collection.aggregate([{
    '$group': {
        '_id': 'null',
        'avg_price': {'$avg': '$price'}
        }}])
    for x in avg_price:
        return(x)
    
def count_median_price(self):
    median_price = self.df['price'].median()
    return(median_price)

    
def count_houses_exposed(self):
    number_houses_exposed = self.collection.aggregate([{'$match': {'last_seen_date': '2023-04-02 20:22:57'}}, {'$count': 'houses_exposed'}])
    for dokument in number_houses_exposed:
        return(dokument)
    
def count_houses_sold(self):
    houses_sold = self.collection.aggregate([{'$match': {'last_seen_date': {'$ne': '2023-04-02 20:22:57'}}}, {'$count': 'houses_sold'}])
    for h_sold in houses_sold:
        return(h_sold)
    
