import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.spiders import CSVFeedSpider
# from myproject.items import TestItem

class MySpider(CSVFeedSpider):
	name = 'example.com'
	allowed_domains = ['example.com']
	start_urls = ['http://www.example.com/feed.csv']
	delimiter = ';'
	quotechar = "'"
	headers = ['id', 'name', 'description']

	def parse_row(self, response, row):
		self.logger.info('Hi, this is a row!: %r', row)

		item = TestItem()
		item['id'] = row['id']
		item['name'] = row['name']
		item['description'] = row['description']
		return item

class TestItem(scrapy.Item):
	id = scrapy.Field()
	name = scrapy.Field()
	description = scrapy.Field()

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(MySpider)
	process.crawl(crawler)
	process.start()
