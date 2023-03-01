
from scrapy import Item, Field


class HouseItem(Item):
    date_str = Field()
    price = Field() 
    url = Field()
    numbers_of_rooms = Field() 
    area = Field() 
    
