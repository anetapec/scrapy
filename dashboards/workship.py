from pymongo import MongoClient
import pandas as pd


# class Collection:                

#     def load_collection(self, collection):    
#         client = MongoClient("mongodb://127.0.0.1:27017")
#         db = client['tricity']
#         self.collection = db[collection]
#         df = pd.DataFrame(list(self.collection.find()))
#         return df     #  => otrzymujemy df z danej kolekcji 
    
    
class House:

    def __init__(self, new_column_name, column_name, column_by_count, frequency):
        self.new_column_name = new_column_name
        self.column_name = column_name
        self.column_by_count = column_by_count
        self.frequency = frequency
        
    def load_collection(self, collection):    
        client = MongoClient("mongodb://127.0.0.1:27017")
        db = client['tricity']
        self.collection = db[collection]
        df = pd.DataFrame(list(self.collection.find()))
        return df     #  => otrzymujemy df z danej kolekcji 
    
    
    # def load_collection(self, collection):
    #     return super().load_collection(collection)  # do tego momentu działa!!!!
    
    def groupped_date(self): 
        house = House(self.new_column_name, self.column_name, self.column_by_count, self.frequency).load_collection(self.collection)
        house[self.new_column_name] = pd.to_datetime(house[self.column_name]) 
        groupped_date_by_freq= house.set_index(self.new_column_name).groupby(pd.Grouper(freq = self.frequency)) 
        return groupped_date_by_freq
    
    def avg_price_by_column(self):
        return self.groupped_date()[self.column_by_count].mean().to_frame().reset_index()

    



# pobieramy dane z kolekcji houses
houses = House(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='D')
print(houses)
#daily_group = houses.load_collection(collection='houses')
#print(daily_group)
print(houses.avg_price_by_column())






#avg_price_by_day  = daily_group    
    
    



