import scrapy
from tricity.items import HouseItem
import re
from datetime import datetime 


class HousesspiderSpider(scrapy.Spider):
    name = 'tricity'
    allowed_domains = ['ogloszenia.trojmiasto.pl']
    start_urls = ['https://ogloszenia.trojmiasto.pl/nieruchomosci/dom/gdynia/']

    
    
    def parse(self, response):
        # Parse each houses 
        houses = response.css('#ogl__list__wrap .list__item')
        
        for house in houses:
            item = HouseItem()
            
            try:
                item['date_str'] = datetime.today().strftime('%Y-%m-%d')
                item['price'] = re.sub("[^0-9]", "", house.css('div.list__item__picture__price').get())
                item['url'] = house.css('a.list__item__content__title__name.link').attrib['href']
                item['numbers_of_rooms'] = re.sub("[^.0-9]", "", house.css('li.list__item__details__icons__element.details--icons--element--l_pokoi').get())
                item['area'] = re.sub("[^.0-9]", "",house.css('p.list__item__details__icons__element__desc::text').get())
               
            
            except: 
                print("-")

            yield item

        '''    
        path_url = response.css('.pages__controls__next ::attr(href)').extract_first()
        base_url = response.url
        next_page = base_url + path_url
        if path_url is not None:
            yield response.follow(next_page, callback=self.parse)
           ''' 