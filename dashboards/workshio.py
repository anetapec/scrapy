import pymongo
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import plotly as go



class DataSource:

    def __init__(self, new_column_name, column_name, column_by_count, frequency):
        self.df = self.load_collection() 
        self.new_column_name = new_column_name
        self.column_name = column_name
        self.column_by_count = column_by_count
        self.frequency = frequency
        

    #connection to the database
    def load_collection(self):
        client = pymongo.MongoClient('mongodb://localhost:27017')
        db = client['tricity']
        self.collection = db['houses']
        df = pd.DataFrame(list(self.collection.find()))
        return df

    def groupped_date(self):  #powstają nowe kolumny datetime i date of sale z danym freq 
        self.df[self.new_column_name] = pd.to_datetime(self.df[self.column_name]) #tworzy nową kolumne grupującą po dniu na podstawie kolumny
        groupped_date_by_freq= self.df.set_index(self.new_column_name).groupby(pd.Grouper(freq = self.frequency)) #grupuje nową kolumnę po dniu lub tyg
        return groupped_date_by_freq
    

    def avg_price_by_column(self):
        return self.df(self.groupped_date(self.column_by_count)).mean().to_frame().reset_index()
    
    def median_by_column(self):
        return self.df[self.groupped_date(self.column_by_count)].median()

    
            
    
daily_avg_price = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='D') 
print(daily_avg_price.groupped_date())
print(daily_avg_price)
print(daily_avg_price)

#gr_scr_date_by_day = data_source.groupped_date(new_column_name='datetime', column_name='scrapping_date', frequency='D')

#avg_cena = gr_scr_date_by_day['price'].mean()
#print(avg_cena)
#print(data_source.groupped_by_day(new_column_name='datetime', column_name='scrapping_date', frequency='D'))

#avg_p = data_source.count_avg_by_column_name(new_column_name='datetime', column_name='scrapping_date', frequency='D')['price']
#print(avg_p)
#avg_by_price = data_source.groupped_by_day['price'].mean
#groupped_scrapping_date_by_day = data_source.groupped_date(new_column_name='datetime', column_name='scrapping_date', frequency='D')
#groupped_scrapping_date_by_week = data_source.groupped_date(new_column_name='datetime', column_name='scrapping_date', frequency='W',) 

# ANALYSIS HOUSES FOR SALE
# Daily prices:

avg_price_by_price_per_meter = groupped_scrapping_date_by_day['price_per_meter'].mean(skipna=True)
print(avg_price_by_price_per_meter)
median_price= groupped_scrapping_date_by_day['price'].median().to_frame().reset_index() 
median_price_by_price_per_meter = groupped_scrapping_date_by_day['price_per_meter'].median().to_frame().reset_index() 
# Weekly prices:
weekly_avg_price = groupped_scrapping_date_by_week['price'].mean().to_frame().reset_index() 
weekly_avg_price_by_price_per_meter = groupped_scrapping_date_by_week['price_per_meter'].mean().to_frame().reset_index() 
weekly_median_price = groupped_scrapping_date_by_week['price'].median().to_frame().reset_index() 
weekly_median_price_by_price_per_meter = groupped_scrapping_date_by_week['price_per_meter'].median().to_frame().reset_index() 
## Number of houses 
daily_number_of_houses_for_sale = groupped_scrapping_date_by_day['scrapping_date'].count().to_frame().reset_index() 
weekly_number_of_houses_for_sale = groupped_scrapping_date_by_week['scrapping_date'].count().to_frame().reset_index() 

# HOUSES SOLD
groupped_last_seen_date_by_day = data_source.groupped_date(new_column_name='date_of_sale', column_name='last_seen_date', frequency='D')
groupped_last_seen_date_by_week = data_source.groupped_date(new_column_name='date_of_sale', column_name='last_seen_date', frequency='W')
older_than = pd.Timestamp.now() - pd.Timedelta(days=1)
houses_sold = data_source.df[(data_source.df['date_of_sale'] <=  older_than)]
houses_sold.to_csv('houses_sold24-04.csv')

# Number of houses sold 


''''
weekly_number_of_houses_sold = groupped_last_seen_date_by_week['last_seen_date'].count().to_frame().reset_index()
weekly_number_of_houses_sold.to_csv('tyg_ilosc_spzedanych.csv')
'''
# Prices of houses sold on particular days
sorted_df = houses_sold.sort_values(by='last_seen_date')

house_prices_sold_on_a_given_day_by_price = sorted_df


house_prices_sold_on_a_given_day_by_price_per_meter = pd.DataFrame(groupped_last_seen_date_by_day['price_per_meter'])
house_prices_sold_on_a_given_day_by_price_per_meter.to_csv('24kwieciem.csv')


app = Dash(__name__)

app.layout = html.Div(children=[

    html.H1('Real estate prices and sales report in Gdynia'),

    html.H3('Analysis of the prices of houses put up for sale'),
    
    html.P('Average daily price of houses for sale'), 
    
    dcc.Graph(
        id='graph1',
        figure=px.line(avg_price, x="datetime", y="price")
        ),

    html.P('Average daily price per meter of houses for sale'),

    dcc.Graph(
        id='graph2',
        figure=px.line(avg_price_by_price_per_meter, x="datetime", y="price_per_meter")
    ),

    html.P('Median daily price of houses for sale'),

    dcc.Graph(
        id='graph3',
        figure=px.line(median_price, x="datetime", y="price")
    ),

    html.P('Median daily price per meter of houses for sale'),

    dcc.Graph(
        id='graph4',
        figure=px.line(median_price_by_price_per_meter, x="datetime", y="price_per_meter")
    ),

    html.P('Average weekly price of houses for sale'),

    dcc.Graph(
        id='graph5',
        figure=px.line(weekly_avg_price, x="datetime", y="price")
    ),

    html.P('Average weekly price per meter of houses for sale'),

    dcc.Graph(
        id='graph6',
        figure=px.line(weekly_avg_price_by_price_per_meter, x="datetime", y="price_per_meter")
    ),

    html.P('Median weekly price of houses for sale'),

    dcc.Graph(
        id='graph7',
        figure=px.line(weekly_median_price , x="datetime", y="price")
    ),

    html.P('Median weekly price per meter of houses for sale'),

    dcc.Graph(
        id='graph8',
        figure=px.line(weekly_median_price_by_price_per_meter , x="datetime", y="price_per_meter")
    ),

    html.H3('Number of houses for sale '),
    
    html.P('Daily number of houses for sale'), 
    
    dcc.Graph(
        id='graph9',
        figure=px.bar(sorted_df, x="last_seen_date", y="price", color="url")
        ),

   ]   
)
 




if __name__ == "__main__":
    app.run_server(debug=False)

    

