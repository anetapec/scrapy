from data_source import DataSource
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime


# HOUSES FOR SALE

# Daily avg price, avg price per meter, median, median price per meter,  number of houses for sale :   
   
houses_daily_group = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='D', name_collection='houses') 
avg_price_by_day = houses_daily_group.avg_price_by_column()
median_price = houses_daily_group.median_by_column()
number_of_houses_for_sale_per_day = houses_daily_group.count_object_for_sale().iloc[1:]


daily_group_per_meter = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price_per_meter', frequency='D', name_collection='houses') 
avg_price_per_meter_by_day = daily_group_per_meter.avg_price_by_column()
median_price_per_meter = daily_group_per_meter.median_by_column()

# Weekly avg price , avg price per meter, median, median price per meter, number of houses for sale :

houses_weekly_group = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='W', name_collection='houses')
avg_price_by_week = houses_weekly_group.avg_price_by_column()
median_price_by_week = houses_weekly_group.median_by_column()
number_of_houses_for_sale_per_week = houses_weekly_group.count_object_for_sale().iloc[1:]

houses_weekly_group_per_meter = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price_per_meter', frequency='W', name_collection='houses')
avg_price_per_meter_by_week = houses_weekly_group_per_meter.avg_price_by_column()
median_price_per_meter_by_week = houses_weekly_group_per_meter.median_by_column()

# Monthly avg price, avg price per meter, median, median price per meter, number of houses for sale :
houses_month_group = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='M', name_collection='houses') 
avg_price_by_month = houses_month_group.avg_price_by_column()
median_price_by_month = houses_month_group.median_by_column()
number_of_houses_for_sale_per_month = houses_month_group.count_object_for_sale().iloc[1:]

houses_month_group_per_meter = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price_per_meter', frequency='M', name_collection='houses')
avg_price_per_meter_by_month = houses_month_group_per_meter.avg_price_by_column()
median_price_per_meter_by_month = houses_month_group_per_meter.median_by_column()


# HOUSES SOLD
houses_group_sold_by_day = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price', frequency='D', name_collection='houses')
houses_group_sold_by_week = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price', frequency='W', name_collection='houses')
houses_group_sold_by_month = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price', frequency='M', name_collection='houses')
# count houses sold:
number_houses_sold_per_day = houses_group_sold_by_day.count_object_sold()
number_houses_sold_per_week = houses_group_sold_by_week.count_object_sold()
number_houses_sold_per_month = houses_group_sold_by_month.count_object_sold()
# average price
daily_avg_price_houses_sold = houses_group_sold_by_day.avg_price_object_sold()
weekly_avg_price_houses_sold = houses_group_sold_by_week.avg_price_object_sold()
monthly_avg_price_houses_sold = houses_group_sold_by_month.avg_price_object_sold()
# median price
daily_median_price_houses_sold = houses_group_sold_by_day.median_price_object_sold()
weekly_median_price_houses_sold  = houses_group_sold_by_week.median_price_object_sold()
monthly_median_price_houses_sold = houses_group_sold_by_month.median_price_object_sold()

# grouping to calculate avg price per meter, median price per meter 
houses_daily_group_per_meter_houses_sold = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price_per_meter', frequency='D', name_collection='houses')
houses_weekly_group_per_meter_houses_sold = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price_per_meter', frequency='W', name_collection='houses')
houses_monthly_group_per_meter_houses_sold = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price_per_meter', frequency='M', name_collection='houses')
# average price per meter , median price per meter 
daily_avg_price_per_meter_houses_sold = houses_daily_group_per_meter_houses_sold.avg_price_object_sold()
weekly_avg_price_per_meter_houses_sold = houses_weekly_group_per_meter_houses_sold.avg_price_object_sold()
monthly_avg_price_per_meter_houses_sold = houses_monthly_group_per_meter_houses_sold.avg_price_object_sold()

daily_median_price_per_meter_houses_sold = houses_daily_group_per_meter_houses_sold.median_price_object_sold()
weekly_median_price_per_meter_houses_sold = houses_weekly_group_per_meter_houses_sold.median_price_object_sold()
monthly_median_price_per_meter_houses_sold = houses_monthly_group_per_meter_houses_sold.median_price_object_sold()
# Prices of houses sold on particular days  
houses_group_sold_by_day.df['date_of_sale'] = pd.to_datetime(houses_group_sold_by_day.df['last_seen_date']) 
older_than = pd.Timestamp.now() - pd.Timedelta(days=1)
houses_sold = houses_group_sold_by_day.df[(houses_group_sold_by_day.df['date_of_sale'] <=  older_than)] #per day
sorted_df = houses_sold.sort_values(by='last_seen_date')




# FLATS FOR SALE

# Daily avg price, avg price per meter, median, median price per meter,  number of flats for sale :   
   
daily_group_flats = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='D', name_collection='flats') 
avg_price_flats_by_day = daily_group_flats.avg_price_by_column()
median_price_flats = daily_group_flats.median_by_column()
number_of_flats_for_sale_per_day = daily_group_flats.count_object_for_sale().iloc[1:]


daily_group_per_meter_flats = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price_per_meter', frequency='D', name_collection='flats') 
avg_price_per_meter_flats_by_day = daily_group_per_meter_flats.avg_price_by_column()
median_price_per_meter_flats = daily_group_per_meter_flats.median_by_column()

# Weekly avg price , avg price per meter, median, median price per meter, number of flats for sale :

flats_weekly_group = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='W', name_collection='flats')
avg_price_flats_by_week = flats_weekly_group.avg_price_by_column()
median_price_flats_by_week = flats_weekly_group.median_by_column()
number_of_flats_for_sale_per_week = flats_weekly_group.count_object_for_sale().iloc[1:]

flats_weekly_group_per_meter = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price_per_meter', frequency='W', name_collection='flats')
avg_price_per_meter_flats_by_week = flats_weekly_group_per_meter.avg_price_by_column()
median_price_per_meter_flats_by_week = flats_weekly_group_per_meter.median_by_column()

# Monthly avg price, avg price per meter, median, median price per meter, number of flats for sale :
flats_month_group = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price', frequency='M', name_collection='flats') 
avg_price_flats_by_month = flats_month_group.avg_price_by_column()
median_price_flats_by_month = flats_month_group.median_by_column()
number_of_flats_for_sale_per_month = flats_month_group.count_object_for_sale().iloc[1:]

flats_month_group_per_meter = DataSource(new_column_name='datetime', column_name='scrapping_date', column_by_count='price_per_meter', frequency='M', name_collection='flats')
avg_price_per_meter_flats_by_month = flats_month_group_per_meter.avg_price_by_column()
median_price_per_meter_flats_by_month = flats_month_group_per_meter.median_by_column()


# FLATS SOLD
flats_group_sold_by_day = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price', frequency='D', name_collection='flats')
flats_group_sold_by_week = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price', frequency='W', name_collection='flats')
flats_group_sold_by_month = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price', frequency='M', name_collection='flats')
# count flats sold:
number_flats_sold_per_day = flats_group_sold_by_day.count_object_sold()
number_flats_sold_per_week = flats_group_sold_by_week.count_object_sold()
number_flats_sold_per_month = flats_group_sold_by_month.count_object_sold()
# average price
daily_avg_price_flats_sold = flats_group_sold_by_day.avg_price_object_sold()
weekly_avg_price_flats_sold = flats_group_sold_by_week.avg_price_object_sold()
monthly_avg_price_flats_sold = flats_group_sold_by_month.avg_price_object_sold()
# median price
daily_median_price_flats_sold = flats_group_sold_by_day.median_price_object_sold()
weekly_median_price_flats_sold  = flats_group_sold_by_week.median_price_object_sold()
monthly_median_price_flats_sold = flats_group_sold_by_month.median_price_object_sold()

# grouping to calculate avg price per meter, median price per meter 
flats_daily_group_per_meter_houses_sold = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price_per_meter', frequency='D', name_collection='flats')
flats_weekly_group_per_meter_houses_sold = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price_per_meter', frequency='W', name_collection='flats')
flats_monthly_group_per_meter_houses_sold = DataSource(new_column_name='date_of_sale', column_name='last_seen_date', column_by_count='price_per_meter', frequency='M', name_collection='flats')
# average price per meter , median price per meter 
daily_avg_price_per_meter_flats_sold = flats_daily_group_per_meter_houses_sold.avg_price_object_sold()
weekly_avg_price_per_meter_flats_sold = flats_weekly_group_per_meter_houses_sold.avg_price_object_sold()
monthly_avg_price_per_meter_flats_sold = flats_monthly_group_per_meter_houses_sold.avg_price_object_sold()

daily_median_price_per_meter_flats_sold = flats_daily_group_per_meter_houses_sold.median_price_object_sold()
weekly_median_price_per_meter_flats_sold = flats_weekly_group_per_meter_houses_sold.median_price_object_sold()
monthly_median_price_per_meter_flats_sold = flats_monthly_group_per_meter_houses_sold.median_price_object_sold()
# Prices of flats sold on particular days  
flats_group_sold_by_day.df['date_of_sale'] = pd.to_datetime(flats_group_sold_by_day.df['last_seen_date']) 
older_than = pd.Timestamp.now() - pd.Timedelta(days=1)
flats_sold = flats_group_sold_by_day.df[(flats_group_sold_by_day.df['date_of_sale'] <=  older_than)] #per day
flats_sorted_df = flats_sold.sort_values(by='last_seen_date')

fig_monthly_median_price_houses_sold = px.bar(monthly_median_price_houses_sold, x="date_of_sale", y="price", 
              labels={"date_of_sale": "Date", "price": "Median price of houses"},
              hover_data={"date_of_sale": "|%B %d, %Y"},
              title='Monthly median price of houses sold.'
              )

fig_monthly_median_price_houses_sold.update_xaxes(
    
    dtick="M1",
    tickformat="%b\n%Y")



app = Dash(__name__)

app.layout = html.Div(children=[

    html.H1('Real estate prices and sales report in Gdynia'),

    html.H3('Analysis of the prices of houses put up for sale'),
    
    

    #html.P('Monthly median price of houses sold'), 
    
    dcc.Graph(
       
        figure=fig_monthly_median_price_houses_sold
    ),
    
    html.P('Average daily price of houses for sale'), 
    
    dcc.Graph(
        id='graph1',
        figure=px.bar(avg_price_by_day , x="datetime", y="price",
                      labels={"datetime": "Date",
                            "price": "Average price of houses"})
                            

    ), 


    html.P('Average daily price per meter of houses for sale'),

    dcc.Graph(
        id='graph2',
        figure=px.bar(avg_price_per_meter_by_day, x="datetime", y="price_per_meter",
                      labels={"datetime": "Date",
                            "price_per_meter": "Average price per meter of houses"})
    ),

    html.P('Median daily price of houses for sale'),

    dcc.Graph(
        id='graph3',
        figure=px.bar(median_price, x="datetime", y="price",
                      labels={"datetime": "Date",
                            "price": "Median price of houses"})
    ),

    html.P('Median daily price per meter of houses for sale'),

    dcc.Graph(
        id='graph4',
        figure=px.bar(median_price_per_meter, x="datetime", y="price_per_meter",
                      labels={"datetime": "Date",
                            "price_per_meter": "Median price per meter of houses"})
    ),

    html.P('Average weekly price of houses for sale'),

    dcc.Graph(
        id='graph5',
        figure=px.bar(avg_price_by_week, x="datetime", y="price",
                      labels={"datetime": "Date",
                            "price": "Average price of houses"})
    ),

    html.P('Average weekly price per meter of houses for sale'),

    dcc.Graph(
        id='graph6',
        figure=px.bar(avg_price_per_meter_by_week, x="datetime", y="price_per_meter",
                      labels={"datetime": "Date",
                            "price_per_meter": "Average price per meter of houses"})
    ),

    html.P('Median weekly price of houses for sale'),

    dcc.Graph(
        id='graph7',
        figure=px.bar(median_price_by_week , x="datetime", y="price",
                      labels={"datetime": "Date",
                            "price": "Median price of houses"})
    ),

    html.P('Median weekly price per meter of houses for sale'),

    dcc.Graph(
        id='graph8',
        figure=px.bar(median_price_per_meter_by_week , x="datetime", y="price_per_meter",
                      labels={"datetime": "Date",
                            "price_per_meter": "Median price per meter of houses"})
    ),


    html.P('Average monthly price of houses for sale'),

    dcc.Graph(
        id='graph9',
        figure=px.bar(avg_price_by_month, x="datetime", y="price",
                      labels={"datetime": "Date",
                            "price": "Average price of houses"})
    ), 

    html.P('Average monthly price per meter of houses for sale'),

    dcc.Graph(
        id='graph10',
        figure=px.bar(avg_price_per_meter_by_month, x="datetime", y="price_per_meter",
                      labels={"datetime": "Date",
                            "price_per_meter": "Average price per meter of houses"})
    ),   

    html.P('Median monthly price of houses for sale'),

    dcc.Graph(
        id='graph11',
        figure=px.bar(median_price_by_month , x="datetime", y="price")
    ),   

    html.P('Median monthly price per meter of houses for sale'),

    dcc.Graph(
        id='graph12',
        figure=px.bar(median_price_per_meter_by_month , x="datetime", y="price_per_meter")
    ),  

    html.P('Number of houses for sale per day'),

    dcc.Graph(
        id='graph13',
        figure=px.bar(number_of_houses_for_sale_per_day , x="datetime", y="scrapping_date", 
                      labels={"datetime": "Date",
                              "scrapping_date": "Number of houses for sale"})
    ),

    html.P('Number of houses for sale per week'), 

    dcc.Graph(
        id='graph14',
        figure=px.bar(number_of_houses_for_sale_per_week , x="datetime", y="scrapping_date",
                      labels={"datetime": "Date",
                            "scrapping_date": "Number of houses for sale"})
    ),

    html.P('Number of houses for sale per month'), 

    dcc.Graph(
        id='graph15',
        figure=px.bar(number_of_houses_for_sale_per_month , x="datetime", y="scrapping_date",
                      labels={"datetime": "Date",
                            "scrapping_date": "Number of houses for sale"})
    ),

    html.H3('Analysis of the prices of houses sold'),
    html.P('Daily price of houses sold.'), 

    dcc.Graph(
        id='graph16',
        figure=px.bar(sorted_df, x="last_seen_date", y="price", color="url")
        ),

    html.P('Daily price_per_meter of houses sold.'), 

    dcc.Graph(
        id='graph17',
        figure=px.bar(sorted_df, x="last_seen_date", y="price_per_meter", color="url")
        ),

    html.P('Weekly average price of houses sold.'), 

    dcc.Graph(
        id='graph18',
        figure=px.bar(weekly_avg_price_houses_sold, x="date_of_sale", y="price")
        ),
    
    html.P('Weekly average price per meter of houses sold'), 

    dcc.Graph(
        id='graph19',
        figure=px.bar(weekly_avg_price_per_meter_houses_sold, x="date_of_sale", y="price_per_meter")
        ),

    html.P('Monthly average price of houses sold.'), 

    dcc.Graph(
        id='graph20',
        figure=px.bar(monthly_avg_price_houses_sold, x="date_of_sale", y="price")
        ),
   
   html.P('Monthly average price per meter of houses sold.'), 

    dcc.Graph(
        id='graph21',
        figure=px.bar(monthly_avg_price_per_meter_houses_sold, x="date_of_sale", y="price_per_meter",
                      labels={"date_of_sale": "Date",
                            "price_per_meter": "Average price per meter of houses"},
                      hover_data={"date_of_sale": "|%B %d , %Y"},  title='Monthly average price per meter of houses sold.'),
        ),
        
    html.P('Daily median price  of houses sold'), 

    dcc.Graph(
        id='graph22',
        figure=px.bar(daily_median_price_houses_sold, x="date_of_sale", y="price")
        ),

    html.P('Daily median price per meter of houses sold'), 

    dcc.Graph(
        id='graph23',
        figure=px.bar(daily_median_price_per_meter_houses_sold, x="date_of_sale", y="price_per_meter")
        ),

    html.P('Weekly median price per meter of houses sold'), 

    dcc.Graph(
        id='graph24',
        figure=px.bar(weekly_median_price_per_meter_houses_sold, x="date_of_sale", y="price_per_meter")
        ),

    html.P('Monthly median price per meter of houses sold'), 

    dcc.Graph(
        id='graph25',
        figure=px.bar(monthly_median_price_per_meter_houses_sold, x="date_of_sale", y="price_per_meter")
        ),




###################################################################################################################

    html.H1('Real estate prices flats and sales report in Gdynia'),
    html.H3('Analysis of the prices of flats put up for sale'),
    html.P('Average daily price of flats for sale'), 
    
    dcc.Graph(
        id='graph26',
        figure=px.bar(avg_price_flats_by_day , x="datetime", y="price")

    ), 

    html.P('Average daily price per meter of flats for sale'),

    dcc.Graph(
        id='graph26-1',
        figure=px.bar(avg_price_per_meter_flats_by_day, x="datetime", y="price_per_meter")
    ),

    html.P('Median daily price of flats for sale'),

    dcc.Graph(
        id='graph27',
        figure=px.bar(median_price_flats, x="datetime", y="price")
    ),

    html.P('Median daily price per meter of flats for sale'),

    dcc.Graph(
        id='graph28',
        figure=px.bar(median_price_per_meter_flats, x="datetime", y="price_per_meter")
    ),

    html.P('Average weekly price of flats for sale'),

    dcc.Graph(
        id='graph29',
        figure=px.bar(avg_price_flats_by_week, x="datetime", y="price")
    ),

    html.P('Average weekly price per meter of flats for sale'),

    dcc.Graph(
        id='graph30',
        figure=px.bar(avg_price_per_meter_flats_by_week, x="datetime", y="price_per_meter")
    ),

    html.P('Median weekly price of flats for sale'),

    dcc.Graph(
        id='graph31',
        figure=px.bar(median_price_flats_by_week , x="datetime", y="price")
    ),

    html.P('Median weekly price per meter of flats for sale'),

    dcc.Graph(
        id='graph32',
        figure=px.bar(median_price_per_meter_flats_by_week , x="datetime", y="price_per_meter")
    ),


    html.P('Average monthly price of flats for sale'),

    dcc.Graph(
        id='graph33',
        figure=px.bar(avg_price_flats_by_month, x="datetime", y="price")
    ), 

    html.P('Average monthly price per meter of flats for sale'),

    dcc.Graph(
        id='graph34',
        figure=px.bar(avg_price_per_meter_flats_by_month, x="datetime" , y="price_per_meter")
    ),   

    html.P('Median monthly price of flats for sale'),

    dcc.Graph(
        id='graph35',
        figure=px.bar(median_price_flats_by_month , x="datetime", y="price")
    ),   

    html.P('Median monthly price per meter of flats for sale'),

    dcc.Graph(
        id='graph36',
        figure=px.bar(median_price_per_meter_flats_by_month , x="datetime", y="price_per_meter")
    ),  

    html.P('Number of flats for sale per day'),

    dcc.Graph(
        id='graph37',
        figure=px.bar(number_of_flats_for_sale_per_day , x="datetime", y="scrapping_date",
                      labels={"datetime": "Date",
                            "scrapping_date": "Number of flat for sale"})
    ),

    html.P('Number of flats for sale per week'), 

    dcc.Graph(
        id='graph38',
        figure=px.bar(number_of_flats_for_sale_per_week , x="datetime", y="scrapping_date",
                      labels={"datetime": "Date",
                            "scrapping_date": "Number of flat for sale"})
    ),

    html.P('Number of flats for sale per month'), 

    dcc.Graph(
        id='graph39',
        figure=px.bar(number_of_flats_for_sale_per_month , x="datetime", y="scrapping_date",
                      labels={"datetime": "Date",
                            "scrapping_date": "Number of flat for sale"})
    ),

    html.H3('Analysis of the prices of flats sold'),
    html.P('Daily price of flats sold.'), 

    dcc.Graph(
        id='graph40',
        figure=px.bar(flats_sorted_df, x="last_seen_date", y="price", color="url")
        ),

    html.P('Daily price_per_meter of flats sold.'), 

    dcc.Graph(
        id='graph41',
        figure=px.bar(flats_sorted_df, x="last_seen_date", y="price_per_meter", color="url")
        ),

    html.P('Weekly average price of flats sold.'), 

    dcc.Graph(
        id='graph42',
        figure=px.bar(weekly_avg_price_flats_sold, x="date_of_sale", y="price")
        ),
    
    html.P('Weekly average price per meter of flats sold'), 

    dcc.Graph(
        id='graph43',
        figure=px.bar(weekly_avg_price_per_meter_flats_sold, x="date_of_sale", y="price_per_meter")
        ),

    html.P('Monthly average price of flats sold.'), 

    dcc.Graph(
        id='graph44',
        figure=px.bar(monthly_avg_price_flats_sold, x="date_of_sale", y="price")
        ),
   
    html.P('Monthly average price per meter of flats sold.'), 

    dcc.Graph(
        id='graph45',
        figure=px.bar(monthly_avg_price_per_meter_flats_sold, x="date_of_sale", y="price_per_meter")
        ),
    
    html.P('Daily median price  of flats sold'), 

    dcc.Graph(
        id='graph46',
        figure=px.bar(daily_median_price_flats_sold, x="date_of_sale", y="price")
        ),

    html.P('Daily median price per meter of flats sold'), 

    dcc.Graph(
        id='graph47',
        figure=px.bar(daily_median_price_per_meter_flats_sold, x="date_of_sale", y="price_per_meter")
        ),

    html.P('Weekly median price per meter of flats sold'), 

    dcc.Graph(
        id='graph48',
        figure=px.bar(weekly_median_price_per_meter_flats_sold, x="date_of_sale", y="price_per_meter")
        ),

    html.P('Monthly median price per meter of flats sold'), 

    dcc.Graph(
        id='graph49',
        figure=px.bar(monthly_median_price_per_meter_flats_sold, x="date_of_sale", y="price_per_meter")
        ),



   
   ]   
)
 

if __name__ == "__main__":
    app.run_server(debug=False)


