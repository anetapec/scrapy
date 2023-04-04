import pymongo
import pandas as pd
import datetime


client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['tricity']
collection = db['houses']
df = pd.DataFrame(list(collection.find()))
'''
# AVG price per meter:
avg_price_per_meter = collection.aggregate([{
    '$group': {
        '_id': '$scrapping_date',
        'avg_price_per_meter': {'$avg': '$price_per_meter'}
    }}])
for x in avg_price_per_meter:
  print(x)
#lub drugi sposób na wyliczenie ceny za metr:
price_per_meter_avg = df['price_per_meter'].mean()
print(f"Średnia cena za metr wynosi: {price_per_meter_avg} zł.")

#mediana z ceny za metr:
median_price_per_meter = df['price_per_meter'].median()
print(f"Mediana z ceny za metr wynosi: {median_price_per_meter} zł.")

#Średnia cena za dom :
avg_price = collection.aggregate([{
    '$group': {
        '_id': '$scrapping_date',
        'avg_price': {'$avg': '$price'}
    }}])
for x in avg_price:
  print(x)
#drugi sposób na wyliczenie średniej ceny
price_avg = df['price'].mean()
print(f"Średnia cena za dom wynosi: {price_avg} zł.")

#mediana z ceny za dom 
median_price = df['price'].median()
print(f"Mediana z ceny za dom wynosi: {median_price} zł.")

# ile jest obecnie wystawionych domów:
number_houses_exposed = collection.aggregate([{'$match': {'last_seen_date': '2023-04-03 19:13:59'}}, {'$count': 'houses_exposed'}])
for dokument in number_houses_exposed:
  print(dokument)
#ile domów się sprzedało:
houses_sold = collection.aggregate([{'$match': {'last_seen_date': {'$gt': ISODate('2023-04-02 20:22:57'), '$lt': ISODate('2023-04-03 19:13:59')}}}, {'$count': 'houses_sold'}])
for h_sold in houses_sold:
  print(h_sold)
''' 
houses_sold = collection.find({
    'last_seen_date': {
        '$gt': ISODate('2023-04-02'),
        '$lt': ISODate('2023-04-03')
    }
})



'''
prices_of_houses_sold = collection.aggregate([{'$match': {'last_seen_date': '2023-04-02 20:22:57'}}])
for _ in prices_of_houses_sold:
  print(_)

#by wyliczyć ilość domów sprzedanych w danym okresie
collection.find({
    'last_seen_date': {
        '$gt': ISODate("2023-04-02 20:22:57"),
        '$lt': ISODate("2023-04-03 19:13:59")
    }
})

''''