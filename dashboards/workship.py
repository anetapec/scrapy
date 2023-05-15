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

    def __init__(self, new_column_name, column_name, column_by_count, frequency, name_collection):
        
        self.name_collection = self.load_collection(name_collection)
        self.new_column_name = new_column_name
        self.column_name = column_name
        self.column_by_count = column_by_count
        self.frequency = frequency
        
    def load_collection(self, name_collection):    
        client = MongoClient("mongodb://127.0.0.1:27017")
        db = client['tricity']
        collection = db[name_collection]
        df = pd.DataFrame(list(collection.find()))
        return df     #  => otrzymujemy df z danej kolekcji 
    
    
    # def load_collection(self, collection):
    #     return super().load_collection(collection)  # do tego momentu działa!!!!
    
    def groupped_date(self): 
        self.df = House(self.new_column_name, self.column_name, self.column_by_count, self.frequency, self.name_collection).load_collection(self.name_collection)
        self.df[self.new_column_name] = pd.to_datetime(self.df[self.column_name]) 
        groupped_date_by_freq=self.df.set_index(self.new_column_name).groupby(pd.Grouper(freq = self.frequency)) 
        return groupped_date_by_freq
    
 
    def avg_price_by_column(self):
        return self.groupped_date()[self.column_by_count].mean().to_frame().reset_index()

    



# pobieramy dane z kolekcji houses
houses = House(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='W', name_collection='houses')

#daily_group = houses.load_collection(collection='houses')
#print(daily_group)
collection_houses = houses.load_collection('houses')
print(collection_houses)  # ładuje kolekcje


#fff = collection_houses()
#print(fff)






# print(avg_price_by_day)

    



