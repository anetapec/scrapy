import scrapy
from tricity.items import HouseItem
import re
import requests


class FlatsspidersSpider(scrapy.Spider):
    name = "flatsspiders"
    allowed_domains = ["dom.trojmiasto.pl"]
    start_urls = ["https://dom.trojmiasto.pl/nieruchomosci-rynek-wtorny/e1i,17_14_13_18_16_24_19_25_6_15_61_20_21,ii,1,qi,45_,wi,100.html"]


    custom_settings = { "collection": "flats"}

    def parse(self, response):
        flats = response.css(".ogloszeniaList__item")
        for flat in flats:
            item = HouseItem()
            try:
                item['price'] = int(re.sub("[^0-9]", "", flat.css("p.ogloszeniaList__price::text").get()))
                item['url'] = flat.css("a.ogloszeniaList__img").attrib["href"]
                item['numbers_of_rooms'] = str(flat.css(".ogloszeniaList__detail.button.button--label.button--fourth:nth-child(2)::text").get()).lstrip()  
                item['area'] = str(flat.css(".ogloszeniaList__detail.button.button--label.button--fourth::text").get()).strip()

            except: 
                print("-")
            yield item

        path_url = response.css(".pagination__controls__next::attr(href)").get()  
        
        base_url = "https://dom.trojmiasto.pl/nieruchomosci-rynek-wtorny/e1i,17_14_13_18_16_24_19_25_6_15_61_20_21,ii,1,qi,45_,wi,100.html"
        next_page = base_url + path_url
        if path_url is not None:
            yield scrapy.Request(next_page, callback=self.parse)
        
        # First attempt to solve:

        # base_url = self.start_urls
        # next_page = base_url + path_url
        # if path_url is not None:
            # yield response.follow(next_page, callback=self.parse)

########################################################################################
        # Second attempt to solve: - to wg mnie nie działa bo w naszym adresie są 
            # przecinki i z tego co wyczytałam to może traktowac adres jako krotkę 
        
        # base_url = requests.post(self.start_urls)    # tu próbowałam też z request.get
        # next_page = base_url.url + path_url
        # if path_url is not None:
            # yield scrapy.Request(next_page, callback=self.parse)


        
    
        
        