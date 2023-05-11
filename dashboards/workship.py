from pymongo import MongoClient
import pandas as pd


class Collection:                

    def load_collection(self, collection):    
        client = MongoClient("mongodb://127.0.0.1:27017")
        db = client['tricity']
        self.collection = db[collection]
        df = pd.DataFrame(list(self.collection.find()))
        return df     #  => otrzymujemy df z danej kolekcji 
    
class House(Collection):

    def __init__(self, new_column_name, column_name, column_by_count, frequency):
        self.new_column_name = new_column_name
        self.column_name = column_name
        self.column_by_count = column_by_count
        self.frequency = frequency
        
    
    def load_collection(self, collection):
        return super().load_collection(collection)  # do tego momentu działa!!!!

    

daily_group  = House(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='D').load_collection(collection='houses')
print(daily_group)    
#avg_price_by_day  = daily_group    
    
    




house = Collection()
print(house.load_collection(collection='houses'))

daily_group = Calculations(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='D')
print(daily_group)

#load_collection()
#client.close()

# proba = load_collection(collection='flats')
# print(proba)