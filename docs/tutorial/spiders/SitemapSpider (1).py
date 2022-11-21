import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.spiders import SitemapSpider
# from myproject.items import TestItem

class MySpider(SitemapSpider):
	sitemap_urls = ['http://www.example.com/sitemap.xml']

	def parse(self, response):
		pass # ... scrape item here ...

class TestItem(scrapy.Item):
	id = scrapy.Field()
	name = scrapy.Field()
	description = scrapy.Field()

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(MySpider)
	process.crawl(crawler)
	process.start()
