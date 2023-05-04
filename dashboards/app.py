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



# ANALYSIS HOUSES FOR SALE
            
# Daily avg price, avg price per meter, median:   
   
daily_group = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='D') 
avg_price_by_day = daily_group.avg_price_by_column()
median_price = daily_group.median_by_column()
number_of_houses_for_sale_per_day = daily_group.count_houses_for_sale()

daily_group_per_meter = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price_per_meter', frequency='D') 
avg_price_per_meter_by_day = daily_group_per_meter.avg_price_by_column()
median_price_per_meter = daily_group_per_meter.median_by_column()



# weekly avg price , avg price per meter, median :

weekly_group = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='W')
avg_price_by_week = weekly_group.avg_price_by_column()
median_price_by_week = weekly_group.median_by_column()
number_of_houses_for_sale_per_week = weekly_group.count_houses_for_sale()

weekly_group_per_meter = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price_per_meter', frequency='W')
avg_price_per_meter_by_week = weekly_group_per_meter.avg_price_by_column()
median_price_per_meter_by_week = weekly_group_per_meter.median_by_column()

# HOUSES SOLD
group_sold_by_day = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price', frequency='D')
group_sold_by_week = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price', frequency='W')

print(group_sold_by_day.skip_unsold_houses())
daily_number_houses_sold = group_sold_by_day.skip_unsold_houses()['last_seen_date'].count().to_frame().reset_index()
print(daily_number_houses_sold)

   






'''

# HOUSES SOLD
groupped_last_seen_date_by_day = data_source.groupped_date(new_column_name='date_of_sale', column_name='last_seen_date', frequency='D')
groupped_last_seen_date_by_week = data_source.groupped_date(new_column_name='date_of_sale', column_name='last_seen_date', frequency='W')
older_than = pd.Timestamp.now() - pd.Timedelta(days=1)
houses_sold = data_source.df[(data_source.df['date_of_sale'] <=  older_than)]
houses_sold.to_csv('houses_sold24-04.csv')

# Number of houses sold 



weekly_number_of_houses_sold = groupped_last_seen_date_by_week['last_seen_date'].count().to_frame().reset_index()
weekly_number_of_houses_sold.to_csv('tyg_ilosc_spzedanych.csv')

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
'''

