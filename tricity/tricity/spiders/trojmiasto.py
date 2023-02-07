import scrapy


class TrojmiastoSpider(scrapy.Spider):
    name = "trojmiasto"
    allowed_domains = ["ogloszenia.trojmiasto.pl"]
    start_urls = ["http://ogloszenia.trojmiasto.pl/"]

    def parse(self, response):
        pass
