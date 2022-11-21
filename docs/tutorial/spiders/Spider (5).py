import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector

class MySpider(scrapy.Spider):
	name = 'myspider'

	def start_requests(self):
		yield scrapy.Request(f'http://www.example.com/categories/{self.category}')

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(MySpider)
	process.crawl(MySpider, category="electronics")
	process.start()

# import scrapy

# class MySpider(scrapy.Spider):
# 	name = 'myspider'

# 	def __init__(self, category=None, *args, **kwargs):
# 		super(MySpider, self).__init__(*args, **kwargs)
# 		self.start_urls = [f'http://www.example.com/categories/{category}']
# 		# ...
# [cmd]
# scrapy crawl myspider -a category=electronics
