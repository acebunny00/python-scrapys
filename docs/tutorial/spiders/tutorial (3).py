import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector

class QuotesSpider(scrapy.Spider):
	name = "quotes3"

	start_urls = [
		"https://quotes.toscrape.com/page/1/",
	]

	def parse(self, response):
		for quote in response.css("div.quote"):
			yield {
				"text": quote.css("span.text::text").get(),
				"author": quote.css("small.author::text").get(),
				"tags": quote.css("div.tags a.tag::text").getall(),
			}

		next_page = response.css("li.next a::attr(href)").get()
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(QuotesSpider)
	process.crawl(crawler)
	process.start()

# [cmd]
# scrapy crawl quotes3 -o quotes3.xml