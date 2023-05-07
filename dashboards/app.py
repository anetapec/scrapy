import pymongo
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go


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
    
    def skip_the_column_first_scraping(self):
        pass 
    
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
   
daily_group = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='D') 
avg_price_by_day = daily_group.avg_price_by_column()
median_price = daily_group.median_by_column()
number_of_houses_for_sale_per_day = daily_group.count_houses_for_sale()

daily_group_per_meter = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price_per_meter', frequency='D') 
avg_price_per_meter_by_day = daily_group_per_meter.avg_price_by_column()
median_price_per_meter = daily_group_per_meter.median_by_column()

# Weekly avg price , avg price per meter, median, median price per meter, number of houses for sale :

weekly_group = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='W')
avg_price_by_week = weekly_group.avg_price_by_column()
median_price_by_week = weekly_group.median_by_column()
number_of_houses_for_sale_per_week = weekly_group.count_houses_for_sale()

weekly_group_per_meter = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price_per_meter', frequency='W')
avg_price_per_meter_by_week = weekly_group_per_meter.avg_price_by_column()
median_price_per_meter_by_week = weekly_group_per_meter.median_by_column()

# Monthly avg price, avg price per meter, median, median price per meter, number of houses for sale :
month_group = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='M') 
avg_price_by_month = month_group.avg_price_by_column()
median_price_by_month = month_group.median_by_column()
number_of_houses_for_sale_per_month = month_group.count_houses_for_sale()

month_group_per_meter = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price_per_meter', frequency='M')
avg_price_per_meter_by_month = month_group_per_meter.avg_price_by_column()
median_price_per_meter_by_month = month_group_per_meter.median_by_column()


# HOUSES SOLD
group_sold_by_day = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price', frequency='D')
group_sold_by_week = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price', frequency='W')
group_sold_by_month = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price', frequency='M')
# count houses sold:
number_houses_sold_per_day = group_sold_by_day.count_houses_sold()
number_houses_sold_per_week = group_sold_by_week.count_houses_sold()
number_houses_sold_per_month = group_sold_by_month.count_houses_sold()
# average price
daily_avg_price_houses_sold = group_sold_by_day.avg_price_houses_sold()
weekly_avg_price_houses_sold = group_sold_by_week.avg_price_houses_sold()
monhly_avg_price_houses_sold = group_sold_by_month.avg_price_houses_sold()
# median price
daily_median_price_houses_sold = group_sold_by_day.median_price_houses_sold()
weekly_median_price_houses_sold  = group_sold_by_week.median_price_houses_sold()
monthly_median_price_houses_sold = group_sold_by_month.median_price_houses_sold()

# grouping to calculate avg price per meter, median price per meter 
daily_group_per_meter_houses_sold = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price_per_meter', frequency='D')
weekly_group_per_meter_houses_sold = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price_per_meter', frequency='W')
monthly_group_per_meter_houses_sold = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price_per_meter', frequency='M')
# average price per meter 
daily_avg_price_per_meter_houses_sold = daily_group_per_meter_houses_sold.avg_price_houses_sold()
weekly_avg_price_per_meter_houses_sold = weekly_group_per_meter_houses_sold.avg_price_houses_sold()
monthly_avg_price_per_meter_houses_sold = monthly_group_per_meter_houses_sold.avg_price_houses_sold()

# Prices of houses sold on particular days  
group_sold_by_day.df['date_of_sale'] = pd.to_datetime(group_sold_by_day.df['last_seen_date']) 
older_than = pd.Timestamp.now() - pd.Timedelta(days=1)
houses_sold = group_sold_by_day.df[(group_sold_by_day.df['date_of_sale'] <=  older_than)] #per day
sorted_df = houses_sold.sort_values(by='last_seen_date')


app = Dash(__name__)

app.layout = html.Div(children=[

    html.H1('Real estate prices and sales report in Gdynia'),

    html.H3('Analysis of the prices of houses put up for sale'),
    
    html.P('Average daily price of houses for sale'), 
    
    dcc.Graph(
        id='graph1',
        figure=px.line(avg_price_by_day , x="datetime", y="price")

    ), 

    html.P('Average daily price per meter of houses for sale'),

    dcc.Graph(
        id='graph2',
        figure=px.line(avg_price_per_meter_by_day, x="datetime", y="price_per_meter")
    ),

    html.P('Median daily price of houses for sale'),

    dcc.Graph(
        id='graph3',
        figure=px.line(median_price, x="datetime", y="price")
    ),

    html.P('Median daily price per meter of houses for sale'),

    dcc.Graph(
        id='graph4',
        figure=px.line(median_price_per_meter, x="datetime", y="price_per_meter")
    ),

    html.P('Average weekly price of houses for sale'),

    dcc.Graph(
        id='graph5',
        figure=px.line(avg_price_by_week, x="datetime", y="price")
    ),

    html.P('Average weekly price per meter of houses for sale'),

    dcc.Graph(
        id='graph6',
        figure=px.line(avg_price_per_meter_by_week, x="datetime", y="price_per_meter")
    ),

    html.P('Median weekly price of houses for sale'),

    dcc.Graph(
        id='graph7',
        figure=px.line(median_price_by_week , x="datetime", y="price")
    ),

    html.P('Median weekly price per meter of houses for sale'),

    dcc.Graph(
        id='graph8',
        figure=px.line(median_price_per_meter_by_week , x="datetime", y="price_per_meter")
    ),


    html.P('Average monthly price of houses for sale'),

    dcc.Graph(
        id='graph9',
        figure=px.line(avg_price_by_month, x="datetime", y="price")
    ), 

    html.P('Average monthly price per meter of houses for sale'),

    dcc.Graph(
        id='graph10',
        figure=px.line(avg_price_per_meter_by_month, x="datetime", y="price_per_meter")
    ),   

    html.P('Median monthly price of houses for sale'),

    dcc.Graph(
        id='graph11',
        figure=px.line(median_price_by_month , x="datetime", y="price")
    ),   

    html.P('Median monthly price per meter of houses for sale'),

    dcc.Graph(
        id='graph12',
        figure=px.line(median_price_per_meter_by_month , x="datetime", y="price_per_meter")
    ),  

    html.P('Number of houses for sale per day'),

    dcc.Graph(
        id='graph13',
        figure=px.line(number_of_houses_for_sale_per_day , x="datetime", y="scrapping_date")
    ),

    html.P('Number of houses for sale per week'), # => trzeba usunąć datę scrapowania wszystkich domów

    dcc.Graph(
        id='graph14',
        figure=px.line(number_of_houses_for_sale_per_week , x="datetime", y="scrapping_date")
    ),

    html.P('Number of houses for sale per month'), # => trzeba usunąć datę scrapowania wszystkich domów

    dcc.Graph(
        id='graph15',
        figure=px.line(number_of_houses_for_sale_per_month , x="datetime", y="scrapping_date")
    ),

    
    html.P('Price of houses sold per day'), 

    dcc.Graph(
        id='graph16',
        figure=px.bar(sorted_df, x="last_seen_date", y="price", color="url")
        ),

    html.P('Price_per_meter of houses sold per day'), 

    dcc.Graph(
        id='graph17',
        figure=px.bar(sorted_df, x="last_seen_date", y="price_per_meter", color="url")
        ),
    
    html.P('Daily weekly price of houses sold'), 

    dcc.Graph(
        id='graph18',
        figure=px.line(weekly_avg_price_houses_sold, x="date_of_sale", y="price")
        ),
   
    

   ]   
)
 

if __name__ == "__main__":
    app.run_server(debug=False)


