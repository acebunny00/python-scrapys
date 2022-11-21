import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
	name = 'example.com'
	allowed_domains = ['example.com']
	start_urls = ['http://www.example.com']

	rules = (
		# 'category.php'일치하는 링크 추출 ('subsection.php'와 일치하지 않음)
		# 그리고 그들로부터 링크를 따르십시오 (콜백이 없기 때문에 기본적으로 다음 = true).
		# Extract links matching 'category.php' (but not matching 'subsection.php')
		# and follow links from them (since no callback means follow=True by default).
		Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

		# 'item.php'일치하는 링크를 추출하고 스파이더의 방법 Parse_item으로 구문 분석합니다.
		# Extract links matching 'item.php' and parse them with the spider's method parse_item
		Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
	)

	def parse_item(self, response):
		self.logger.info('Hi, this is an item page! %s', response.url)
		item = scrapy.Item()
		item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
		item['name'] = response.xpath('//td[@id="item_name"]/text()').get()
		item['description'] = response.xpath('//td[@id="item_description"]/text()').get()
		item['link_text'] = response.meta['link_text']
		url = response.xpath('//td[@id="additional_data"]/@href').get()
		return response.follow(url, self.parse_additional_page, cb_kwargs=dict(item=item))

	def parse_additional_page(self, response, item):
		item['additional_data'] = response.xpath('//p[@id="additional_data"]/text()').get()
		return item

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(MySpider)
	process.crawl(crawler)
	process.start()
