import scrapy

class SqueegeeSpider(scrapy.Spider):
    name = 'Squeegee'
    start_urls = ['https://www.randomlists.com/email-addresses?qty=100']

    def parse(self, response):
        print(response.text)