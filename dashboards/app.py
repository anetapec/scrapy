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

#converting an object 'scrapping_date' from a date in a string to a Date Time object
data_source.df['datetime'] = pd.to_datetime(data_source.df['scrapping_date']) 
#print(data_source.df['datetime'])
#grouping dates by day
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
#sale prices of houses on particular days
#price_sold_houses = daily_number_of_houses_sold_df.groupby(data_source.df['last_seen']('price'))
#print(price_sold_houses)


#daily_sale_prices_of_houses_sold = groupped_last_seen_date_by_day['last_seen_date'].count()
# Number of houses sold per week   
groupped_last_seen_date_by_week = data_source.df.set_index('last_seen').groupby(pd.Grouper(freq='W'))
weekly_number_of_houses_sold = groupped_last_seen_date_by_week['last_seen_date'].count()
print(weekly_number_of_houses_sold)
  
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
        

'''''

])
'''
        #html.Table([
        #   html.Tr([html.Th(col) for col in data_source.df.columns])] + 
        #    [html.Tr([html.Td(data_source.df.iloc[i][col]) for col in data_source.df.columns])for i in range(min_val)]
        

# dcc.Graph(
#     figure=go.Figure(
#         data=[
#             go.Bar(
#                 x=data_source.df['datetime'],
#                 y=data_source.df[avg_price_by_price],
#                 name='Average price of housing' 
#             )
#         ],
#         layout=go.Layout(
#                 yaxis_type='log',
#                 height=300,
#                 title_text='Mean for price per day of houseses sold'
#         ) 
#     )
# )
        


if __name__ == "__main__":
    app.run_server(debug=False)



