import scrapy
from tricity.items import HouseItem

class HousesspiderSpider(scrapy.Spider):
    name = 'tricity'
    allowed_domains = ['ogloszenia.trojmiasto.pl']
    start_urls = ['https://ogloszenia.trojmiasto.pl/nieruchomosci/dom/gdynia/']

    def parse(self, response):
        houses = response.css('#ogl__list__wrap .list__item')

        for house in houses:
            house_item = HouseItem()
            house_item['price'] = house.css('.list__item__picture__price p::text').extract_first()
            house_item['price_per_meter'] = response.css('p.list__item__details__info.details--info--price::text').get().replace('zł/m', '')
            house_item['url'] = response.css('a.list__item__content__title__name.link').attrib['href']
            house_item['area'] = response.xpath("//p[@class='list__item__details__icons__element__desc']//text()").get().replace('\n                                            ', '').replace('\n                                    ', '')
            house_item['number_of_rooms'] = response.xpath('//ul/li[2]/div/p[2]//text()').get().replace('\n                                            ', '').replace('\n                                    ', '')

            yield house_item

        next_page = response.css('span.pages__item__active').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

            

            