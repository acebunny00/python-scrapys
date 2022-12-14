import scrapy

class Product(scrapy.Item):
	name = scrapy.Field()
	price = scrapy.Field()
	stock = scrapy.Field()
	tags = scrapy.Field()
	last_updated = scrapy.Field(serializer=str)
