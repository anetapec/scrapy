from scrapy import Item, Field


class FlatItem(Item):
    price = Field() 
    #price_per_meter = Field()
    url = Field()
    numbers_of_rooms = Field() 
    area = Field() 
    #scrapping_date = Field()
    #hash = Field()
    #last_seen_date = Field()