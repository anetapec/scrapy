
from scrapy import Item, Field


class HouseItem(Item):
    price = Field()
    #price_per_meter = Field()
    url = Field()
    area = Field()
    #numbers_of_rooms = Field()
