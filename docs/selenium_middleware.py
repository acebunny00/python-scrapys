from time import sleep
 
from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.utils.python import to_bytes
 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumMiddleware(object):
	@classmethod
	def from_crawler(cls, crawler):
		middleware = cls()
		crawler.signals.connect(middleware.spider_opened, signals.spider_opened)	# Crawler가 실행될 때, Spider가 생성되면 middleware의 spider_opened를 실행되도록 설정.
		crawler.signals.connect(middleware.spider_closed, signals.spider_closed)	# Crawler가 실행될 때, Spider가 종료되면 middleware의 spider_closed를 실행되도록 설정.
		return middleware
 
	def spider_opened(self, spider):
		WINDOW_SIZE = "1920,1080"

		# chrome_options = Options()
		# chrome_options.add_argument("--headless")		# 크롬창이 열리지 않음
		# chrome_options.add_argument("--no-sandbox")		# GUI를 사용할 수 없는 환경에서 설정, linux, docker 등
		# chrome_options.add_argument("--disable-gpu")	# GUI를 사용할 수 없는 환경에서 설정, linux, docker 등
		# chrome_options.add_argument(f"--window-size={ WINDOW_SIZE }")
		# chrome_options.add_argument("Content-Type=application/json; charset=utf-8")
		# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

		driver = webdriver.Chrome(ChromeDriverManager().install())
		driver.get("https://quotes.toscrape.com")
		self.driver = driver
 
	def spider_closed(self, spider):
		self.driver.close()
 
	def process_request( self, request, spider ):	# Spider가 start_requests에서 Request를 던지면 이 함수로 넘어옴.
		self.driver.get( request.url )	# 요청한 주소를 다시 Selenium으로 Reqeust를 던짐.
		body = to_bytes( text=self.driver.page_source )	# process_request는 HtmlResponse를 반환하는데 이때 body가 'bytes' 타입이여야 함.
		sleep( 5 )
		return HtmlResponse( url=request.url, body=body, encoding='utf-8', request=request )	# Selenium 으로 요청한 결과로 새로운 Response를 생성하여 반환.