# 항목 파이프라인 구성 요소 활성화

import scrapy
class DocsScrapySpider(scrapy.Spider):
	custom_settings = {
		"ITEM_PIPELINES": {
			'myproject.pipelines.PricePipeline': 300,
			'myproject.pipelines.JsonWriterPipeline': 800,
		},
	}
