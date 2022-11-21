# scrapy genspider -t basic Basic quotes.toscrape.com
# scrapy genspider Basic quotes.toscrape.com

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector


class BasicSpider(scrapy.Spider):
	name = 'Basic'
	allowed_domains = ['quotes.toscrape.com']
	start_urls = ['http://quotes.toscrape.com/']

	def parse(self, response):
		pass

	# # scrapy glance	https://docs.scrapy.org/en/latest/intro/overview.html
	# start_urls = [
	# 	"https://quotes.toscrape.com/tag/humor/",
	# ]
	# # tutorial1		https://docs.scrapy.org/en/latest/intro/tutorial.html
	# def start_requests(self):
	# 	urls = [
	# 		"https://quotes.toscrape.com/page/1/",
	# 		"https://quotes.toscrape.com/page/2/",
	# 	]
	# 	for url in urls:
	# 		yield scrapy.Request(url=url, callback=self.parse)
	# # tutorial2
	# start_urls = [
	# 	"https://quotes.toscrape.com/page/1/",
	# 	"https://quotes.toscrape.com/page/2/",
	# ]
	# # tutorial3
	# start_urls = [
	# 	"https://quotes.toscrape.com/page/1/",
	# ]
	# # tutorial4
	# start_urls = [
	# 	"https://quotes.toscrape.com/page/1/",
	# ]
	# # tutorial5
	# start_urls = ["https://quotes.toscrape.com/"]
	# # tutorial6
	# def start_requests(self):
	# 	url = "https://quotes.toscrape.com/"
	# 	tag = getattr(self, "tag", None)
	# 	if tag is not None:
	# 		url = url + "tag/" + tag
	# 	yield scrapy.Request(url, self.parse)

	# # scrapy glance	https://docs.scrapy.org/en/latest/intro/overview.html
	# def parse(self, response):
	# 	for quote in response.css("div.quote"):
	# 		yield {
	# 			"author": quote.xpath("span/small/text()").get(),
	# 			"text": quote.css("span.text::text").get(),
	# 		}
	# 	next_page = response.css("li.next a::attr('href')").get()
	# 	if next_page is not None:
	# 		yield response.follow(next_page, self.parse)
	# # tutorial1		https://docs.scrapy.org/en/latest/intro/tutorial.html
	# def parse(self, response):
	# 	page = response.url.split("/")[-2]
	# 	filename = f"out_tutorial1-{page}.html"
	# 	with open(filename, "wb") as f:
	# 		f.write(response.body)
	# 	self.log(f"Saved file {filename}")
	# # tutorial2
	# def parse(self, response):
	# 	for quote in response.css("div.quote"):
	# 		yield {
	# 			"text": quote.css("span.text::text").get(),
	# 			"author": quote.css("small.author::text").get(),
	# 			"tags": quote.css("div.tags a.tag::text").getall(),
	# 		}
	# # tutorial3
	# def parse(self, response):
	# 	for quote in response.css("div.quote"):
	# 		yield {
	# 			"text": quote.css("span.text::text").get(),
	# 			"author": quote.css("small.author::text").get(),
	# 			"tags": quote.css("div.tags a.tag::text").getall(),
	# 		}
	# 	next_page = response.css("li.next a::attr(href)").get()
	# 	if next_page is not None:
	# 		next_page = response.urljoin(next_page)
	# 		yield scrapy.Request(next_page, callback=self.parse)
	# # tutorial4
	# def parse(self, response):
	# 	for quote in response.css("div.quote"):
	# 		yield {
	# 			"text": quote.css("span.text::text").get(),
	# 			"author": quote.css("span small::text").get(),
	# 			"tags": quote.css("div.tags a.tag::text").getall(),
	# 		}
	# 	next_page = response.css("li.next a::attr(href)").get()
	# 	if next_page is not None:
	# 		yield response.follow(next_page, callback=self.parse)
	# # tutorial5
	# def parse(self, response):
	# 	author_page_links = response.css(".author + a")
	# 	yield from response.follow_all(author_page_links, self.parse_author)
	# 	pagination_links = response.css("li.next a")
	# 	yield from response.follow_all(pagination_links, self.parse)
	# def parse_author(self, response):
	# 	def extract_with_css(query):
	# 		return response.css(query).get(default="").strip()
	# 	yield {
	# 		"name": extract_with_css("h3.author-title::text"),
	# 		"birthdate": extract_with_css(".author-born-date::text"),
	# 		"bio": extract_with_css(".author-description::text"),
	# 	}
	# # tutorial6
	# def parse(self, response):
	# 	for quote in response.css("div.quote"):
	# 		yield {
	# 			"text": quote.css("span.text::text").get(),
	# 			"author": quote.css("small.author::text").get(),
	# 		}
	# 	next_page = response.css("li.next a::attr(href)").get()
	# 	if next_page is not None:
	# 		yield response.follow(next_page, self.parse)

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(BasicSpider)
	process.crawl(crawler)
	process.start()

# scrapy crawl Basic -O Basic.csv
