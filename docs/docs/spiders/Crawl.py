# scrapy genspider -t crawl Crawl quotes.toscrape.com

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector


class CrawlSpider(CrawlSpider):
	name = 'Crawl'

	## custom_settings
	project_name = __file__.split("\\")[-4]
	output_dir_deploy = "_data/"
	output_dir_debug = project_name + "/"+ output_dir_deploy
	output_dir = output_dir_debug if __name__ == "__main__" else output_dir_deploy
	output_file_name = "%(name)s_%(time)s"
	output_file_name = name
	output_path = output_dir + output_file_name
	output_file_org = output_path + " - org.html"

	custom_settings = {
		"ROBOTSTXT_OBEY": False,
		"LOG_LEVEL": "INFO",

		## 데이터형 출력 파일은 세팅만으로 OK
		"FEED_EXPORT_ENCODING": "utf-8",
		"FEEDS": {
			output_path + ".csv": {"format": "csv", "encoding": "cp949", "overwrite": True},
			output_path + ".xml": {"format": "xml", "encoding": "utf-8", "overwrite": True},
			output_path + ".json": {"format": "json", "encoding": "utf-8", "overwrite": True},
			# output_path + ".jsonl": {"format": "jsonl", "encoding": "utf-8", "overwrite": True},
		},

		# https://github.com/alecxe/scrapy-fake-useragent
		"DOWNLOADER_MIDDLEWARES": {
			'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
			'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
			'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
			'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
		},
		"FAKEUSERAGENT_PROVIDERS": [
			'scrapy_fake_useragent.providers.FakeUserAgentProvider',	# 이것은 우리가 시도해 볼 첫 번째 제공자입니다. # this is the first provider we'll try
			'scrapy_fake_useragent.providers.FakerProvider',			# FakeUserAgentProvider가 실패하면 Faker를 사용하여 사용자 에이전트 문자열을 생성합니다. # if FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
			'scrapy_fake_useragent.providers.FixedUserAgentProvider',	# user_agent 값으로 돌아갑니다. # fall back to USER_AGENT value
		],
	}

	settings_add_debug = {
		"LOG_LEVEL": "DEBUG",
		"LOG_ENCODING": "utf-8",
		"LOG_FILE": "scrapy.log",
		"LOG_FILE_APPEND": False,
	}

	settings_add_deploy = {
		## 기타 출력 파일은 프로젝트의 파이프라인 클래스를 만듦
		# "ITEM_PIPELINES": {
		# 	"tutorial.pipelines.MarkDownWriterPipeline": 300,
		# 	"tutorial.pipelines.HTMLWriterPipeline": 300,
		# 	},
	}

	custom_settings = dict(custom_settings, **settings_add_debug) if __name__ == "__main__" else dict(custom_settings, **settings_add_deploy)

	allowed_domains = ['quotes.toscrape.com']
	start_urls = ['http://quotes.toscrape.com/']

	rules = (
		Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
	)

	def parse_item(self, response):
		item = {}
		#item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
		#item['name'] = response.xpath('//div[@id="name"]').get()
		#item['description'] = response.xpath('//div[@id="description"]').get()
		return item

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(CrawlSpider)
	process.crawl(crawler)
	process.start()

# scrapy crawl Crawl
