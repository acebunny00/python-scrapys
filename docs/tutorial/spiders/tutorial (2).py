import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector

class QuotesSpider(scrapy.Spider):
	name = "quotes2"

	start_urls = [
		"https://quotes.toscrape.com/page/1/",
		"https://quotes.toscrape.com/page/2/",
	]

	def parse(self, response):
		for quote in response.css("div.quote"):
			yield {
				"text": quote.css("span.text::text").get(),
				"author": quote.css("small.author::text").get(),
				"tags": quote.css("div.tags a.tag::text").getall(),
			}

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(QuotesSpider)
	process.crawl(crawler)
	process.start()

# [cmd]
# scrapy crawl quotes2 -O quotes2.jsonl
# scrapy crawl quotes2 -o quotes2.jsonl

# [log]
# 2016-09-19 18:57:19 [scrapy.core.scraper] DEBUG: Scraped from <200 https://quotes.toscrape.com/page/1/>
# {'tags': ['life', 'love'], 'author': 'André Gide', 'text': '“It is better to be hated for what you are than to be loved for what you are not.”'}
# 2016-09-19 18:57:19 [scrapy.core.scraper] DEBUG: Scraped from <200 https://quotes.toscrape.com/page/1/>
# {'tags': ['edison', 'failure', 'inspirational', 'paraphrased'], 'author': 'Thomas A. Edison', 'text': "“I have not failed. I've just found 10,000 ways that won't work.”"}