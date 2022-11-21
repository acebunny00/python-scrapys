import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.spiders import XMLFeedSpider
# from myproject.items import TestItem

class MySpider(XMLFeedSpider):
	name = 'example.com'
	allowed_domains = ['example.com']
	start_urls = ['http://www.example.com/feed.xml']
	iterator = 'iternodes'  # 이것은 실제로 불필요합니다. 기본값이기 때문입니다. # This is actually unnecessary, since it's the default value
	itertag = 'item'

	def parse_node(self, response, node):
		self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))

		item = TestItem()
		item['id'] = node.xpath('@id').get()
		item['name'] = node.xpath('name').get()
		item['description'] = node.xpath('description').get()
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
