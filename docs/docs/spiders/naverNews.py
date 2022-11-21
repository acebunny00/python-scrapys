import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime as dt
 
class NaverNewsSpider(scrapy.Spider):																									# scrapy.Spider를 상속받음. 부모의 메소드 중 start_requests를 재정의하여 사용할 계획.
	name = 'NaverNews'																													# Spider의 이름으로써 실행할 때 사용할 명칭.
	allowed_domains = ['news.naver.com']																								# allowed_domains - 접근 가능한 도메인 목록. 크롤러가 접근 도메인이 목록에 없으면 접근이 제한됨. 생략가능.
 
	def __init__(self, *args, **kargs):																									# Spider가 생성될 때 실행되는 함수로 초기값을 지정할 때 사용.
		today = dt.now().strftime('%Y%m%d')																								# 현재 년월일 구하기.
		pages = [ 1, 2, 3 ]																												# page를 따로 크롤링하지 않기 때문에 강제적으로 지정.
 
		self.start_urls = []
		for page in pages:
			# self.start_urls.append(																										# start_urls - 데이터를 수집할 url의 목록으로 start_requests에서 사용됨.
			# 	f'https://news.naver.com/main/list.nhn?mode=LSD&mid=shm&sid1=105&sid2=731&listType=title&date={ today }&page={ page }'	# 위에서 지정한 페이지 수 만큼 start_url을 설정함.
			# )
			self.start_urls.append(
				f'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105#&date=%2000:00:00&page={ page }'
			)
 
	def start_requests(self):																											# Spider가 실행되면 start_requests 함수가 호출되며, HttpResponse를 반환.
		for url in self.start_urls:
			yield scrapy.Request( url=url, callback=self.parse, method='GET', encoding='utf-8')											# yield는 현재 함수를 제너레이터(Generator)로 만드는 키워드이며, 단순하게 실행결과를 여러번 반환 한다고 생각하자.( 제너레이터는 다른 포스트에서 다루도록 하겠음. )
																																		# scrapy.Request( ... callback=self.parse ... ) callback은 결과값을 반환할 함수를 설정, request의 결과를 parse로 받음.
 
	def parse(self, response):																											# def parse(self, response) - start_requests에서 보낸 요청에 대한 응답을 처리하는 함수.
																																		# 위에서 실행한 Request의 결과를 처리하는 함수로 Item 또는 Dict 을 반환.
		# contents = response.xpath('//*[@id="main_content"]/div[1]/ul/li')																# xpath를 이용해서 뉴스의 목록만 수집.
		contents = response.xpath('//*[@id="main_content"]')

		for content in contents:
			# title = content.xpath('a/text()').extract_first()																			# 목록에서 뉴스를 하나씩 뽑아내면서 제목과 작성자 데이터를 수집. xpath의 결과값은 list이며 extract_first로 첫번째 값만 뽑아냄.
			# author = content.xpath('span[1]/text()').extract_first()
			title = content.xpath('/ul/li/dl/dt[2]/a/text()').extract_first()
			author = content.xpath('/ul/li/dl/dd/span[2]/text()').extract_first()
 
			item = {																													# 추출한 데이터를 Dict에 저장, 추후 Item에 Schema를 정의해서 변경.
				'title': title.strip() if title else title,
				'author': author.strip() if author else author
			}
			print( item )
 
			yield item
if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(NaverNewsSpider)
	process.crawl(crawler)
	process.start()
