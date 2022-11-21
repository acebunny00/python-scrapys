import scrapy

class Product(scrapy.Item):
	name = scrapy.Field()
	price = scrapy.Field()
	stock = scrapy.Field()
	tags = scrapy.Field()
	last_updated = scrapy.Field(serializer=str)

class DiscountedProduct(Product):
	discount_percent = scrapy.Field(serializer=str)
	discount_expiration_date = scrapy.Field()

class SpecificProduct(Product):
	name = scrapy.Field(Product.fields['name'], serializer=my_serializer)
