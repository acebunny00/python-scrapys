import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector

class MySpider(scrapy.Spider):
	name = 'example.com'
	allowed_domains = ['example.com']
	start_urls = [
		'http://www.example.com/1.html',
		'http://www.example.com/2.html',
		'http://www.example.com/3.html',
	]

	def parse(self, response):
		self.logger.info('A response from %s just arrived!', response.url)

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(MySpider)
	process.crawl(crawler)
	process.start()
