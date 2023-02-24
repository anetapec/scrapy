
from scrapy import Item, Field


class HouseItem(Item):
    price = Field() 
    url = Field()
    numbers_of_rooms = Field() 
    area = Field() 
    
