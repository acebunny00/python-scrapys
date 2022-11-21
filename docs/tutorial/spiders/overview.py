import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector

class QuotesSpider(scrapy.Spider):
	name = "tutorial_overview"
	start_urls = [
		"https://quotes.toscrape.com/tag/humor/",
	]

	def parse(self, response):
		for quote in response.css("div.quote"):
			yield {
				"author": quote.xpath("span/small/text()").get(),
				"text": quote.css("span.text::text").get(),
			}

		next_page = response.css("li.next a::attr('href')").get()
		if next_page is not None:
			yield response.follow(next_page, self.parse)

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(QuotesSpider)
	process.crawl(crawler)
	process.start()

# [cmd]
# scrapy runspider tutorial\spiders\tutorial_overview.py -o tutorial_overview.jsonl

# [log]
# {"author": "Jane Austen", "text": "\u201cThe person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.\u201d"}
# {"author": "Steve Martin", "text": "\u201cA day without sunshine is like, you know, night.\u201d"}
# {"author": "Garrison Keillor", "text": "\u201cAnyone who thinks sitting in church can make you a Christian must also think that sitting in a garage can make you a car.\u201d"}
# ...
