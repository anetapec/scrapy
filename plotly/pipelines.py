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




''''
def count_houses_exposed(self):
    houses_seen_today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    number_houses_exposed = self.df.aggregate([{'$match': {'last_seen_date': houses_seen_today}}, {'$count': 'houses_exposed'}])
    return number_houses_exposed

def count_houses_sold(self):
    
'''