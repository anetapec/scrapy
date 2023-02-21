import scrapy
from tricity.items import HouseItem
import re
import json
import hashlib


class HousesspiderSpider(scrapy.Spider):
    name = 'tricity'
    allowed_domains = ['ogloszenia.trojmiasto.pl']
    start_urls = ['https://ogloszenia.trojmiasto.pl/nieruchomosci/dom/gdynia/']

    
    
    def parse(self, response):
        houses = response.css('#ogl__list__wrap .list__item')
        
        for house in houses:
            house_item = HouseItem()
            
            try:
                
                house_item['price'] = re.sub("[^0-9]", "", house.css('div.list__item__picture__price').get())
                house_item['url'] = house.css('a.list__item__content__title__name.link').attrib['href']
                house_item['numbers_of_rooms'] = re.sub("[^.0-9]", "", house.css('li.list__item__details__icons__element.details--icons--element--l_pokoi').get())
                house_item['area'] = re.sub("[^.0-9]", "",house.css('p.list__item__details__icons__element__desc::text').get())
                #house_item['price_per_meter'] = float(round((house_item['price']) / float(house_item['area'])), 2)
                house_item['price_per_meter'] = float(house_item['price']) / float(house_item['area'])
            
            except: 
                print("-")

            yield house_item

            
        path_url = response.css('.pages__controls__next ::attr(href)').extract_first()
        base_url = response.url
        next_page = base_url + path_url
        if path_url is not None:
            yield response.follow(next_page, callback=self.parse)

        for house_item in HouseItem():
            try:
                item = {house_item["price"]: house_item["url"]}
                result = hashlib.md5(json.dumps(item, sort_keys=True).encode('utf-8'))
                hash_value = result.hexdigest
                print(hash_value)
            except:
                print(" - ")
            