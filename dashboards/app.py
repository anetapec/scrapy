import pymongo
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import plotly as go

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

# Houses for sale:

data_source = DataSource()

# converting an object 'scrapping_date' from a date in a string to a Date Time object 'datetime'
data_source.df['datetime'] = pd.to_datetime(data_source.df['scrapping_date']) 
# grouping by day 
groupped_scraping_date_by_day = data_source.df.set_index('datetime').groupby(pd.Grouper(freq='D'))
# Average daily price of houses for sale
avg_price_by_price = groupped_scraping_date_by_day['price'].mean()
avg_price_by_price_df = avg_price_by_price.to_frame().reset_index()
# Average daily price per meter of houses for sale
avg_price_by_price_per_meter = groupped_scraping_date_by_day['price_per_meter'].mean()
avg_price_by_price_per_meter_df = avg_price_by_price_per_meter.to_frame().reset_index()
# Median daily price of houses for sale
median_price_by_price = groupped_scraping_date_by_day['price'].median()
median_price_by_price_df = median_price_by_price.to_frame().reset_index()
# Median daily price per meter of houses for sale
median_price_by_price_per_meter = groupped_scraping_date_by_day['price_per_meter'].mean()
median_price_by_price_per_meter_df = median_price_by_price_per_meter.to_frame().reset_index()

# Weekly prices:

# grouping by week
groupped_scraping_date_by_week = data_source.df.set_index('datetime').groupby(pd.Grouper(freq='W'))
# Average weekly price of houses for sale
weekly_avg_price_by_price = groupped_scraping_date_by_week['price'].mean()
weekly_avg_price_by_price_df = weekly_avg_price_by_price.to_frame().reset_index()
# Average weekly price per meter of houses for sale
weekly_avg_price_by_price_per_meter = groupped_scraping_date_by_week['price_per_meter'].mean()
weekly_avg_price_by_price_per_meter_df = weekly_avg_price_by_price_per_meter.to_frame().reset_index()
# Median weekly price of houses for sale
weekly_median_price_by_price = groupped_scraping_date_by_week['price'].median()
weekly_median_price_by_price_df = weekly_median_price_by_price.to_frame().reset_index()
# Median weekly price per meter of houses for sale
weekly_median_price_by_price_per_meter = groupped_scraping_date_by_week['price_per_meter'].median()
weekly_median_price_by_price_per_meter_df = weekly_median_price_by_price_per_meter.to_frame().reset_index()

# Number of houses for sale 

# Daily number of houses for sale  
daily_number_of_houses_for_sale = groupped_scraping_date_by_day['scrapping_date'].count()
daily_number_of_houses_for_sale_df = daily_number_of_houses_for_sale.to_frame().reset_index()
# Weekly number of houses for sale 
weekly_number_of_houses_for_sale = groupped_scraping_date_by_week['scrapping_date'].count()
weekly_number_of_houses_for_sale_df = weekly_number_of_houses_for_sale.to_frame().reset_index()


# Home sales analysis

# converting an object 'last_seen_date' from a date in a string to a Date Time object 'date_of_sale;
data_source.df['date_of_sale'] = pd.to_datetime(data_source.df['last_seen_date']) 
older_than = pd.Timestamp.now() - pd.Timedelta(days=1)
houses_sold = data_source.df[(data_source.df['date_of_sale'] <=  older_than)]

# grouping by day 
groupped_last_seen_date_by_day = houses_sold.set_index('date_of_sale').groupby(pd.Grouper(freq='D'))

# Number of houses sold per day
daily_number_of_houses_sold = groupped_last_seen_date_by_day['last_seen_date'].count()
daily_number_of_houses_sold_df = daily_number_of_houses_sold.to_frame().reset_index()
# Prices of houses sold on particular days
house_prices_sold_on_a_given_day_by_price = pd.DataFrame(groupped_last_seen_date_by_day['price'])
# Prices per meter of houses sold on particular days
house_prices_sold_on_a_given_day_by_price_per_meter = pd.DataFrame(groupped_last_seen_date_by_day['price_per_meter'])

# grouping by weekly 
groupped_last_seen_date_by_week = houses_sold.set_index('date_of_sale').groupby(pd.Grouper(freq='W'))
# Number of houses sold per week
weekly_number_of_houses_sold = groupped_last_seen_date_by_week['last_seen_date'].count()
weekly_number_of_houses_sold_df = weekly_number_of_houses_sold.to_frame().reset_index()








app = Dash(__name__)

app.layout = html.Div(children=[

    html.H1('Real estate prices and sales report in Gdynia'),

    html.H3('Analysis of the prices of houses put up for sale'),
    
    html.P('Average daily price of houses for sale'), 
    
    dcc.Graph(
        id='graph1',
        figure=px.line(avg_price_by_price_df, x="datetime", y="price")
        ),

    html.P('Average daily price per meter of houses for sale'),

    dcc.Graph(
        id='graph2',
        figure=px.line(avg_price_by_price_per_meter_df, x="datetime", y="price_per_meter")
    ),

    html.P('Median daily price of houses for sale'),

    dcc.Graph(
        id='graph3',
        figure=px.line(median_price_by_price_df, x="datetime", y="price")
    ),

    html.P('Median daily price per meter of houses for sale'),

    dcc.Graph(
        id='graph4',
        figure=px.line(median_price_by_price_per_meter_df, x="datetime", y="price_per_meter")
    ),

    html.P('Average weekly price of houses for sale'),

    dcc.Graph(
        id='graph5',
        figure=px.line(weekly_avg_price_by_price_df, x="datetime", y="price")
    ),

    html.P('Average weekly price per meter of houses for sale'),

    dcc.Graph(
        id='graph6',
        figure=px.line(weekly_avg_price_by_price_per_meter_df, x="datetime", y="price_per_meter")
    ),

    html.P('Median weekly price of houses for sale'),

    dcc.Graph(
        id='graph7',
        figure=px.line(weekly_median_price_by_price_df , x="datetime", y="price")
    ),

    html.P('Median weekly price per meter of houses for sale'),

    dcc.Graph(
        id='graph8',
        figure=px.line(weekly_median_price_by_price_per_meter_df , x="datetime", y="price_per_meter")
    ),

    html.H3('Number of houses for sale '),
    
    html.P('Daily number of houses for sale'), 
    
    dcc.Graph(
        id='graph9',
        figure=px.line(daily_number_of_houses_for_sale_df, x="datetime", y="scrapping_date")
        ),

    html.P('Weekly number of houses for sale'), 
    
    dcc.Graph(
        id='graph10',
        figure=px.line(weekly_number_of_houses_for_sale_df, x="datetime", y="scrapping_date")
        ),

    html.H3('Hauses sales analysis'),
    
    html.P('Number of houses sold per day'), 
    
    dcc.Graph(
        id='graph11',
        figure=px.line(daily_number_of_houses_sold_df, x="date_of_sale", y="last_seen_date")
        ),

    html.P('Number of houses sold per week'), 
    
    dcc.Graph(
        id='graph12',
        figure=px.line(weekly_number_of_houses_sold_df, x="date_of_sale", y="last_seen_date")
        ),

]   
)


     








if __name__ == "__main__":
    app.run_server(debug=False)
