import scrapy
from tricity.items import HouseItem
import re


class HousesspiderSpider(scrapy.Spider):
    name = 'tricity'
    allowed_domains = ['ogloszenia.trojmiasto.pl']
    start_urls = ['https://ogloszenia.trojmiasto.pl/nieruchomosci/dom/gdynia/']

    
    
    def parse(self, response):
        houses = response.css('#ogl__list__wrap .list__item')
        
        for house in houses:
            house_item = HouseItem()

            house_item['price'] = re.sub("[^0-9]", "", house.css('div.list__item__picture__price').get())
            #house_item['price_per_meter'] = house.css('p.list__item__details__info.details--info--price::text').get()
            house_item['url'] = house.css('a.list__item__content__title__name.link').attrib['href']
            house_item['area'] = re.sub("[^0-9]", "",house.css('p.list__item__details__icons__element__desc::text').get())
            #house_item['number_of_rooms'] = house.css('p.list__item__details__icons__element__desc::text')[1].get()

            yield house_item
                
            


            
        

            
            

            

            