from pymongo import MongoClient
import pandas as pd


class House:

    def __init__(self, new_column_name, column_name, column_by_count, frequency, name_collection):
        
        self.df = self.load_collection(name_collection)
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
        #self.df = House(self.new_column_name, self.column_name, self.column_by_count, self.frequency, self.name_collection).load_collection(self.name_collection)
        
        self.df[self.new_column_name] = pd.to_datetime(self.df[self.column_name]) 
        groupped_date_by_freq=self.df.set_index(self.new_column_name).groupby(pd.Grouper(freq = self.frequency)) 
        return groupped_date_by_freq
    
 
    def avg_price_by_column(self):
        return self.groupped_date()[self.column_by_count].mean().to_frame().reset_index()

    def median_by_column(self):
        return self.groupped_date()[self.column_by_count].median().to_frame().reset_index()

    def count_houses_for_sale(self):
        return self.groupped_date()[self.column_name].count().to_frame().reset_index()
    
    def skip_unsold_houses(self):
        self.df[self.new_column_name] = pd.to_datetime(self.df[self.column_name]) 
        older_than = pd.Timestamp.now() - pd.Timedelta(days=1)
        houses_sold = self.df[(self.df[self.new_column_name] <=  older_than)]
        groupped_date_by_freq= houses_sold.set_index(self.new_column_name).groupby(pd.Grouper(freq = self.frequency))
        return groupped_date_by_freq  
    
    def count_houses_sold(self):
        return self.skip_unsold_houses()[self.column_name].count().to_frame().reset_index()
    
    def avg_price_houses_sold(self):
        return self.skip_unsold_houses()[self.column_by_count].mean().to_frame().reset_index()
    
    def median_price_houses_sold(self):
        return self.skip_unsold_houses()[self.column_by_count].median().to_frame().reset_index()


# HOUSES FOR SALE

# Daily avg price, avg price per meter, median, median price per meter,  number of houses for sale :   

houses_by_column_price = House(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='D', name_collection='houses')

avg_price_by_day = houses_by_column_price.avg_price_by_column()
median_price = houses_by_column_price.median_by_column()
number_of_houses_for_sale_per_day = houses_by_column_price.count_houses_for_sale().iloc[1:]

houses_by_column_price_per_meter = House(new_column_name='datetime', column_name='scrapping_date', column_by_count='price_per_meter', frequency='D', name_collection='houses')

avg_price_per_meter_by_day = houses_by_column_price_per_meter.avg_price_by_column()
median_price_per_meter = houses_by_column_price_per_meter.median_by_column()

# Weekly avg price , avg price per meter, median, median price per meter, number of houses for sale :

week_houses_by_column_price = House(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='W', name_collection='houses')

avg_price_by_week = week_houses_by_column_price.avg_price_by_column()
median_price_by_week = week_houses_by_column_price.median_by_column()
number_of_houses_for_sale_per_week = week_houses_by_column_price.count_houses_for_sale().iloc[1:]

week_houses_by_column_price_per_meter = House(new_column_name='datetime', column_name='scrapping_date', column_by_count='price_per_meter', frequency='W', name_collection='houses')

avg_price_per_meter_by_week = week_houses_by_column_price_per_meter.avg_price_by_column()
median_price_per_meter_by_week = week_houses_by_column_price_per_meter.median_by_column()

# Monthly avg price, avg price per meter, median, median price per meter, number of houses for sale :








'''
# pobieramy dane z kolekcji houses
houses = House(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='W', name_collection='houses')

#daily_group = houses.load_collection(collection='houses')
#print(daily_group)
avg = houses.avg_price_by_column()
print(avg)




# print(avg_price_by_day)

'''    


