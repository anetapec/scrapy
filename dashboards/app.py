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
# Daily prices:

# converting an object 'scrapping_date' from a date in a string to a Date Time object
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







app = Dash(__name__)

app.layout = html.Div(children=[

    html.H1('Real estate prices and sales report in Gdynia'),

    html.H3('Houses for sale'),
    
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

]   
)


     








if __name__ == "__main__":
    app.run_server(debug=False)
