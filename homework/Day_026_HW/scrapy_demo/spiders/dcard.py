import scrapy
from scrapy_demo.items import ScrapyDemoItem

class DcardSpider(scrapy.Spider):
    name = 'dcard'
    allowed_domains = ['www.dcard.tw']
    start_urls = ['http://www.dcard.tw/f/mood/p/236242218']

    def parse(self, response):
        item = ScrapyDemoItem()
        item['title'] = response.xpath('//h1[@class="sc-1932jlp-0 cqaWIE"]/text()').get()
        item['content'] = response.xpath('//div[@class="sc-1npvbtq-0 gfjrnD"]//div//span/text()').getall()
        print(item)
        pass