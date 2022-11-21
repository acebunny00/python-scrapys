import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
	sitemap_urls = ['http://www.example.com/sitemap.xml']
	sitemap_rules = [
		('/product/', 'parse_product'),
		('/category/', 'parse_category'),
	]

	def parse_product(self, response):
		pass # ... scrape product ...

	def parse_category(self, response):
		pass # ... scrape category ...

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(MySpider)
	process.crawl(crawler)
	process.start()
