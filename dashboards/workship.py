from pymongo import MongoClient
import pandas as pd


class Collection:                

    def load_collection(self, name_collection):    
        client = MongoClient("mongodb://127.0.0.1:27017")
        db = client['tricity']
        self.collection = db[name_collection]
        df = pd.DataFrame(list(self.collection.find()))
        return df     #  => otrzymujemy df z danej kolekcji 
    
class House(Collection):

    def __init__(self, new_column_name, column_name, column_by_count, frequency, name_collection):
        self.new_column_name = new_column_name
        self.column_name = column_name
        self.column_by_count = column_by_count
        self.frequency = frequency
        self.df = super().load_collection(name_collection)
        
    
    def load_collection(self, name_collection):
        return super().load_collection(name_collection)  # do tego momentu działa!!!!

    def groupped_date(self): 
        #self.df = self.load_collection()
        self.df[self.new_column_name] = pd.to_datetime(self.df[self.column_name]) 
        groupped_date_by_freq= self.df.set_index(self.new_column_name).groupby(pd.Grouper(freq = self.frequency)) 
        return groupped_date_by_freq
    
    def avg_price_by_column(self):
        return self.groupped_date()[self.column_by_count].mean().to_frame().reset_index()
    

house = House(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='W', name_collection='houses')
group_by_week = house.groupped_date()
print(group_by_week)

avg = house.avg_price_by_column()
print(avg)

