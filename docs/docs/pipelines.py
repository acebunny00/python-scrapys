# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DocsPipeline:
	def process_item(self, item, spider):
		return item




## 마크다운 파일 생성
class MarkDownWriterPipeline:
	def open_spider(self, spider):
		path = "_data"
		self.file = open(path + "\\" + spider.name + ".md", "w", encoding="utf-8")

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):
		adapter = ItemAdapter(item)

		url = str(adapter["url"])
		depth = str(adapter["markdown_depth"])
		title = str(adapter["header_text"])
		codes = str(adapter["codes_text"])

		if depth != "#" :
			self.file.write(depth + " " + title + "\n\n")
		else:
			self.file.write(depth + " [" + title + "](" + url + ")\n\n")

		if codes != "[]":
			for code in adapter["codes_text"]:
				self.file.write("```py\n" + code + "```\n\n")
		return item

## html 파일 생성
class HTMLWriterPipeline:
	head_include = False
	def open_spider(self, spider):
		path = "_data"
		self.file = open(path + "\\" + spider.name + ".html", "w", encoding="utf-8")

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):
		adapter = ItemAdapter(item)

		url = str(adapter["url"])
		head = str(adapter["head"])
		header_depth = str(adapter["header_depth"])
		header_text = str(adapter["header_text"])
		codes = adapter["codes"]

		if not self.head_include :
			self.file.write(head + "\n")
			self.head_include = not self.head_include

		if header_depth != "1" :
			self.file.write("<h" + header_depth + ">" + header_text + "</h" + header_depth + ">\n")
		else:
			self.file.write("<h" + header_depth + "><a href ='" + url + "'>" + header_text + "</a></h" + header_depth + ">\n")

		if codes != "[]":
			for code in codes:
				self.file.write("<section>" + code + "</section>\n")
		return item
