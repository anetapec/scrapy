import pymongo
import pandas as pd
from dash import Dash, html, dcc
import matplotlib.pyplot as plt

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
    

data_source = DataSource()
#converting an object from a date in a string to a Date Time object
data_source.df['datetime'] = pd.to_datetime(data_source.df['scrapping_date']) 
print(data_source.df['datetime'])
#grouping dates by day
groupped_scraping_date_by_day = data_source.df.set_index('datetime').groupby(pd.Grouper(freq='D'))
# Mean for price per day of houseses sold
avg_price_by_price = groupped_scraping_date_by_day['price'].mean().astype(int) #change float=>int
print(avg_price_by_price)

#grouping dates by day
groupped_scraping_date_by_day = data_source.df.set_index('datetime').groupby(pd.Grouper(freq='D'))
# Mean for price per day of houseses sold
avg_price_by_price = groupped_scraping_date_by_day['price'].mean().astype(int) #change float=>int
print(avg_price_by_price)
# Mean for price_per_meter per day of houseses sold
avg_price_by_price_per_meter = groupped_scraping_date_by_day['price_per_meter'].mean().astype(int)
print(avg_price_by_price_per_meter)
# Median for price per day of houseses sold
median_price_by_price = groupped_scraping_date_by_day['price'].median().astype(int)
print(median_price_by_price)
# Median for price_per_meter per day of houseses sold
median_price_by_price_per_meter = groupped_scraping_date_by_day['price_per_meter'].mean().astype(int)
print(median_price_by_price_per_meter)
    
app = Dash(__name__)

app.layout = html.Div(
    children = [
        html.H1(children='Average house price analysis',),
        html.P(
            children='Analysis of the average sale price of houses during the day',
        ),
    
    dcc.Graph(
        figure={
            'avg_price_by_price': [
                {
                    'x': data_source.df['datetime'],
                    'y': avg_price_by_price,
                    'type': 'lines'
                }
            ],
        }
    ),
])
if __name__ == "__main__":
    app.run_server(debug=True)
