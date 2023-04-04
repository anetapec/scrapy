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

if __name__ == '__main__':
    data_source = DataSource()
    avg_by_price = data_source.df.groupby('scrapping_date')['price'].mean()
    avg_by_price_per_meter = data_source.df.groupby('scrapping_date')['price_per_meter'].mean()
    median_by_price = data_source.df.groupby('scrapping_date')['price'].median()
    median_by_price_per_meter = data_source.df.groupby('scrapping_date')['price_per_meter'].median()
    number_houses_exposed = data_source.df.value_counts('last_seen_date')['2023-04-04 21:53:02']
    data_source.df['last_seen_date'] = data_source.df['last_seen_date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
    data_source.df.set_index('last_seen_date', inplace=True)
    houses_sold_in_a_period_of_time = data_source.df.sort_index().loc['2023-04-02':'2023-04-03']
    number_houses_sold_per_week = len(houses_sold_in_a_period_of_time)
    daily_number_of_houses_sold = len(data_source.df.sort_index().loc['2023-04-02'])

    