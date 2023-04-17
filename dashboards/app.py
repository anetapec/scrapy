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
    
    
data_source = DataSource()
## house prices sold per day
# 1) daily mean price 
daily_avg_price_house_sold = data_source.df.groupby('last_seen_date')['price'].mean()
print(daily_avg_price_house_sold)
# 2) daily mean price per meter
daily_avg_price_per_meter_house_sold = data_source.df.groupby('last_seen_date')['price_per_meter'].mean() 
print(daily_avg_price_per_meter_house_sold)

# Converting an object 'last_seen_date' from a date in a string to a Date Time object
data_source.df['last_seen_date'] = pd.to_datetime(data_source.df['last_seen_date'], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
#print(data_source.df)

# filtr last_seen_date by date
house_prices_sold_on_a_given_day= data_source.df[(data_source.df['last_seen_date'] == '2023-04-12')]
# 3) house prices sold on a given day
house_prices_sold_on_a_given_day_by_price = house_prices_sold_on_a_given_day['price']
print(house_prices_sold_on_a_given_day_by_price)# Listed house prices by date
# 4)house prices_per_meters sold on a given day
house_prices_sold_on_a_given_day_by_price_per_meter = house_prices_sold_on_a_given_day['price_per_meter']
print(house_prices_sold_on_a_given_day_by_price_per_meter)#

#houses for sale in the time range
#converting an object 'scrapping_date' from a date in a string to a Date Time object
data_source.df['datetime'] = pd.to_datetime(data_source.df['scrapping_date']) 
#print(data_source.df['datetime'])
#grouping dates by daytyp = data_source.df['last_seen_date'].value_counts().reset_index()

groupped_scraping_date_by_day = data_source.df.set_index('datetime').groupby(pd.Grouper(freq='D'))


# Mean for price per day of houseses sold
avg_price_by_price = groupped_scraping_date_by_day['price'].mean() #change float=>int


#print(avg_price_by_price)

#grouping dates by day
groupped_scraping_date_by_day = data_source.df.set_index('datetime').groupby(pd.Grouper(freq='D'))
# Mean for price per day of houseses sold
avg_price_by_price = groupped_scraping_date_by_day['price'].mean() #change float=>int
#print(avg_price_by_price)
# Mean for price_per_meter per day of houseses sold
avg_price_by_price_per_meter = groupped_scraping_date_by_day['price_per_meter'].mean()
#print(avg_price_by_price_per_meter)
# Median for price per day of houseses sold
median_price_by_price = groupped_scraping_date_by_day['price'].median()
#print(median_price_by_price)
# Median for price_per_meter per day of houseses sold
median_price_by_price_per_meter = groupped_scraping_date_by_day['price_per_meter'].mean()
#print(median_price_by_price_per_meter)

# Grouping dates by week
groupped_scraping_date_by_week = data_source.df.set_index('datetime').groupby(pd.Grouper(freq='W'))
# Weekly number of houses for sale 
weekly_number_of_houses_for_sale = groupped_scraping_date_by_week['scrapping_date'].count()
#print(weekly_number_of_houses_for_sale)

# Daily number of houses for sale
daily_number_of_houses_for_sale = groupped_scraping_date_by_day['scrapping_date'].count()
#print(daily_number_of_houses_for_sale)

# Converting an object 'last_seen_date' from a date in a string to a Date Time object
data_source.df['last_seen'] = pd.to_datetime(data_source.df['last_seen_date'])
groupped_last_seen_date_by_day = data_source.df.set_index('last_seen').groupby(pd.Grouper(freq='D'))

# Number of houses sold per day
daily_number_of_houses_sold = groupped_last_seen_date_by_day['last_seen_date'].count()
daily_number_of_houses_sold_df = daily_number_of_houses_sold.to_frame().reset_index()
print(daily_number_of_houses_sold_df)
daily_number_of_houses_sold_df.to_csv('daily_number_sold.csv')
#df_daily_price_houses_sold = pd.DataFrame(daily_number_of_houses_sold_df['last_seen_date'])['price'].groupby('last_seen_date')
df_daily_price_houses_sold = daily_number_of_houses_sold_df[daily_number_of_houses_sold_df.last_seen!='2023-04-16']
print(df_daily_price_houses_sold)
df_daily_price_houses_sold.to_csv('df_daily_price_houses_sold.csv')

#daily_sale_prices_of_houses_sold = groupped_last_seen_date_by_day['last_seen_date'].count()
# Number of houses sold per week   
groupped_last_seen_date_by_week = data_source.df.set_index('last_seen').groupby(pd.Grouper(freq='W'))
weekly_number_of_houses_sold = groupped_last_seen_date_by_week['last_seen_date'].count()
weekly_number_of_houses_sold_df = weekly_number_of_houses_sold.to_frame().reset_index()
print(weekly_number_of_houses_sold_df)
  
app = Dash(__name__)

avg_price_by_price_df = avg_price_by_price.to_frame().reset_index()
print(avg_price_by_price_df)
fig = px.line(avg_price_by_price_df, x="datetime", y="price")

avg_price_by_price_per_meter_df = avg_price_by_price_per_meter.to_frame().reset_index()
fig_ppm = px.line(avg_price_by_price_per_meter_df, x="datetime", y="price_per_meter")

app.layout = html.Div(children=[
    html.H4('Average house price analysis'),
    html.P('Analysis of the average sale price of houses during the day'),
    html.H2('Mean for price per day of houseses sold'),
    dcc.Graph(
        id='example-graph1',
        figure=px.line(avg_price_by_price_df, x="datetime", y="price")
        )],
)

app.layout = html.Div(children=[
    html.P('Mean for price_per_meter per day of houseses sold'),
    dcc.Graph(
        id='exampe-graph2',
        figure=px.line(avg_price_by_price_per_meter_df, x="datetime", y="price_per_meter")
    )]

    )
        


        


if __name__ == "__main__":
    app.run_server(debug=False)



 