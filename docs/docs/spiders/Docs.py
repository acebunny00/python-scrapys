import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import w3lib.html
from urllib import parse
from pathlib import Path

def url_decode(url):
	decode = parse.unquote(url, encoding="UTF=8")
	decode = decode.replace("&lt;","<").replace("&gt;",">").replace("&amp;","&")
	decode = decode.replace("&nbsp;"," ").replace("&quot;","\"").replace("&#039;","\'")
	decode = decode.replace("&rarr;","→").replace("&euro;","€")
	return decode

class DocsSpider(scrapy.Spider):
	project_name = __file__.split("\\")[-4]
	class_name = __qualname__.replace("Spider","")
	name = 'Docs'

	## custom_settings
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
			output_path + ".csv": {"format": "csv", "encoding": "utf-8", "overwrite": False},
			output_path + ".xml": {"format": "xml", "encoding": "utf-8", "overwrite": False},
			output_path + ".json": {"format": "json", "encoding": "utf-8", "overwrite": False},
			output_path + ".jsonl": {"format": "jsonl", "encoding": "utf-8", "overwrite": False},
		},
	}

	settings_add_debug = {
		"LOG_LEVEL": "DEBUG",
		"LOG_ENCODING": "utf-8",
		"LOG_FILE": "python.log",
		"LOG_FILE_APPEND": False,
	}

	settings_add_deploy = {
		## 기타 출력 파일은 프로젝트의 파이프라인 클래스를 만듦
		"ITEM_PIPELINES": {
			"docs.pipelines.MarkDownWriterPipeline": 300,
			"docs.pipelines.HTMLWriterPipeline": 300,
			},
	}

	custom_settings = dict(custom_settings, **settings_add_debug) if __name__ == "__main__" else dict(custom_settings, **settings_add_deploy)

	HEADER_REGEX = r"<[Hh]\d>.*?<\/[Hh]\d>"
	make_header = True
	make_contents = True
	make_full_page = True
	if make_full_page:
		## 빈 파일 생성
		Path(output_dir).mkdir(exist_ok=True)
		with open(output_file_org, "w", encoding='utf-8') as f:
			f.write("")
		head_included = False


	start_urls = ["https://docs.python.org/3/tutorial/index.html"]
	start_urls = ["https://docs.scrapy.org/en/latest/index.html"]

	def parse(self, response):

		head = Selector(text=str(response.body, "utf-8")).xpath("//head")
		head_html = ""
		body = Selector(text=str(response.body, "utf-8")).xpath("//body")
		url_root = response.urljoin("/")
		url_root_content = str(response.url)[:str(response.url).rfind("/")] + "/"
		contents = body.xpath('//section')
		contents_code = '//*[@class="highlight"]'
		if "scrapy" in response.url: del contents[0]

		# ################################
		# #### href, src test
		# ################################
		# _src = body.xpath("//@src").getall()
		# for i in range(len(_src)-1, -1, -1):
		# 	if "http" in _src[i]:
		# 		del _src[i]
		# _src.sort(reverse=True)
		# _href = body.xpath("//@href").getall()
		# for i in range(len(_href)-1, -1, -1):
		# 	if "http" or "#" in _href[i]:
		# 		del _href[i]
		# _href.sort(reverse=True)
		# ################################
		# ################################

		if self.make_full_page:
			## head
			if not self.head_included:
				head_html = head.get() + "\n"
				head_html = head_html.replace("href=\"_", "href=\"" + url_root_content + "_")
				head_html = head_html.replace("src=\"_", "src=\"" + url_root_content + "_")
				head_html = head_html.replace("href=\"../", "href=\"" + url_root)
				head_html = head_html.replace("src=\"../",  "src=\"" + url_root)
				head_html = head_html.replace("href=\"//", "href=\"" + url_root)
				head_html = head_html.replace("src=\"//", "src=\"" + url_root)
				head_html = head_html.replace("href=\"/", "href=\"" + url_root)
				head_html = head_html.replace("src=\"/", "src=\"" + url_root)
				self.head_included = True

			## href 절대경로 및 타이틀
			split = "href="
			contents_html = contents.get().split(split)
			for ii, s in enumerate(contents_html):
				ss = s.split("\"")
				if ss[0] == '':
					ss[1] = url_root_content + ss[1]
					if "#" in ss[1]:
						ss[1] = ss[1][ss[1].find("#"):]
				sss = "\"".join(ss)
				contents_html[ii] = sss
			contents_html = split.join(contents_html)
			contents_html = contents_html.replace("href=\"_", "href=\"" + url_root_content + "_")
			contents_html = contents_html.replace("src=\"_", "src=\"" + url_root_content + "_")
			contents_html = contents_html.replace("href=\"../", "href=\"" + url_root)
			contents_html = contents_html.replace("src=\"../", "src=\"" + url_root)
			contents_html = contents_html.replace("href=\"//", "href=\"" + url_root)
			contents_html = contents_html.replace("src=\"//", "src=\"" + url_root)
			contents_html = contents_html.replace("href=\"/", "href=\"" + url_root)
			contents_html = contents_html.replace("src=\"/", "src=\"" + url_root)

			with open(self.output_file_org, "a+", encoding='utf-8') as f:
				f.write(head_html + contents_html)

		for i, content in enumerate(contents):
			url = response.url
			content = Selector(text=content.get())
			header = Selector(text=content.re(self.HEADER_REGEX)[0])
			aa = header.get()
			header_depth = int(header.get()[14:15])
			markdown_depth = header_depth * "#"
			header_href = header.xpath("//@href").get()
			header_text = header.xpath("//text()").getall()
			header_text = "".join(header_text[:len(header_text)-1])
			codes = content.xpath(contents_code).getall()
			codes_text = content.xpath(contents_code).getall()

			for i, code in enumerate(codes):
				codes_text[i] = w3lib.html.remove_tags(code)
				codes_text[i] = url_decode(codes_text[i])


			yield {
				"url": url,
				"head": head_html,
				"markdown_depth": markdown_depth,
				"header_depth": header_depth,
				"header_text": header_text,
				"header_href": header_href,
				"codes": codes,
				"codes_text": codes_text,
				"index": i + 1,
			}

		if "python" in response.url: next_page = body.xpath("/html/body/div[4]/ul/li[3]/a/@href").get()
		elif "scrapy" in response.url: next_page = body.xpath('//*[@class="btn btn-neutral float-right"]/@href').get()
		
		if next_page is not None:
			print(next_page)

			yield response.follow(next_page, self.parse)

if __name__ == "__main__":
	process = CrawlerProcess()
	crawler = process.create_crawler(DocsSpider)
	process.crawl(crawler)
	process.start()
