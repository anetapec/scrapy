from pymongo import MongoClient
import pandas as pd
from datetime import datetime
import os 

class DataSource:

    def __init__(self, new_column_name, column_name, column_by_count, frequency, name_collection):
        
        self.df = self.load_collection(name_collection)
        self.new_column_name = new_column_name
        self.column_name = column_name
        self.column_by_count = column_by_count
        self.frequency = frequency
        
    def load_collection(self, name_collection):    
        mongo_uri = os.getenv("MONGO_URI","mongodb://127.0.0.1:27017")
        client = MongoClient(mongo_uri)
        db = client['tricity']
        collection = db[name_collection]
        df = pd.DataFrame(list(collection.find()))
        return df     
    
    def groupped_date(self): 
        self.df[self.new_column_name] = pd.to_datetime(self.df[self.column_name]) 
        groupped_date_by_freq=self.df.set_index(self.new_column_name).groupby(pd.Grouper(freq = self.frequency)) 
        return groupped_date_by_freq

    def avg_price_by_column(self):
        return self.groupped_date()[self.column_by_count].mean().to_frame().reset_index()
    
    def median_by_column(self):
        return self.groupped_date()[self.column_by_count].median().to_frame().reset_index()

    def count_object_for_sale(self):
        return self.groupped_date()[self.column_name].count().to_frame().reset_index()
    
    def skip_unsold_object(self):
        self.df[self.new_column_name] = pd.to_datetime(self.df[self.column_name]) 
        older_than = pd.Timestamp.now() - pd.Timedelta(days=1)
        houses_sold = self.df[(self.df[self.new_column_name] <=  older_than)]
        groupped_date_by_freq= houses_sold.set_index(self.new_column_name).groupby(pd.Grouper(freq = self.frequency))
        return groupped_date_by_freq  
    
    def count_object_sold(self):
        return self.skip_unsold_object()[self.column_name].count().to_frame().reset_index()
    
    def avg_price_object_sold(self):
        return self.skip_unsold_object()[self.column_by_count].mean().to_frame().reset_index()
    
    def median_price_object_sold(self):
        return self.skip_unsold_object()[self.column_by_count].median().to_frame().reset_index()