import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector

class QuotesSpider(scrapy.Spider):
	name = "quotes1"

	def start_requests(self):
		urls = [
			"https://quotes.toscrape.com/page/1/",
			"https://quotes.toscrape.com/page/2/",
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = f"quotes1-{page}.html"
		with open(filename, "wb") as f:
			f.write(response.body)
		self.log(f"Saved file {filename}")

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(QuotesSpider)
	process.crawl(crawler)
	process.start()

# [cmd]]
# scrapy crawl quotes1

# [log]
# ... (omitted for brevity)
# 2016-12-16 21:24:05 [scrapy.core.engine] INFO: Spider opened
# 2016-12-16 21:24:05 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
# 2016-12-16 21:24:05 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
# 2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://quotes.toscrape.com/robots.txt> (referer: None)
# 2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://quotes.toscrape.com/page/1/> (referer: None)
# 2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://quotes.toscrape.com/page/2/> (referer: None)
# 2016-12-16 21:24:05 [quotes] DEBUG: Saved file quotes1-1.html
# 2016-12-16 21:24:05 [quotes] DEBUG: Saved file quotes1-2.html
# 2016-12-16 21:24:05 [scrapy.core.engine] INFO: Closing spider (finished)
# ...
