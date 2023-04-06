import pymongo
import pandas as pd
from datetime import datetime

class DataSource:

    def __init__(self):
        self.df = self.load_collection() 

    #connection to the database
    def load_collection(self):
        client = pymongo.MongoClient('mongodb://localhost:27017')
        db = client['tricity']
        self.collection = db['houses']
        df = pd.DataFrame(list(self.collection.find()))
        return df
# Mean for price per day of houseses sold
# Median for price per day of houseses sold

if __name__ == '__main__':
    data_source = DataSource()
    print(data_source.df['scrapping_date'])
    data_source.df['datetime'] = pd.to_datetime(data_source.df['scrapping_date']) 
    print(data_source.df['datetime'])
    groupped_by_day = data_source.df.set_index('datetime').groupby(pd.Grouper(freq='D'))
    avg_price_by_price = groupped_by_day['price'].mean().astype(int)
    print(avg_price_by_price)
    