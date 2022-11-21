import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
# from myproject.items import MyItem

class MySpider(scrapy.Spider):
	name = 'example.com'
	allowed_domains = ['example.com']

	def start_requests(self):
		yield scrapy.Request('http://www.example.com/1.html', self.parse)
		yield scrapy.Request('http://www.example.com/2.html', self.parse)
		yield scrapy.Request('http://www.example.com/3.html', self.parse)

	def parse(self, response):
		for h3 in response.xpath('//h3').getall():
			yield MyItem(title=h3)

		for href in response.xpath('//a/@href').getall():
			yield scrapy.Request(response.urljoin(href), self.parse)

class MyItem(scrapy.Item):
	title = scrapy.Field()

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(MySpider)
	process.crawl(crawler)
	process.start()
