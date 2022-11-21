import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector

class MySpider(scrapy.Spider):
	name = 'myspider'

	def start_requests(self):
		return [
			scrapy.FormRequest("http://www.example.com/login",
			formdata={'user': 'john', 'pass': 'secret'},
			callback=self.logged_in),
		]

	def logged_in(self, response):
		# 여기에서 링크를 추출하여 각각의 콜백을 통해 각각에 대한 요청을 반환하고 반환합니다.
		# here you would extract links to follow and return Requests for each of them, with another callback
		pass

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(MySpider)
	process.crawl(crawler)
	process.start()
