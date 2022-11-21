import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
	sitemap_urls = ['http://www.example.com/robots.txt']
	sitemap_rules = [
		('/shop/', 'parse_shop'),
	]
	sitemap_follow = ['/sitemap_shops']

	def parse_shop(self, response):
		pass # ... scrape shop here ...

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(MySpider)
	process.crawl(crawler)
	process.start()
