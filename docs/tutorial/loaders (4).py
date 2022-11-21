import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

def filter_price(value):
	if value.isdigit():
		return value

class Product(scrapy.Item):
	name = scrapy.Field(
		input_processor=MapCompose(remove_tags),
		output_processor=Join(),
	)
	price = scrapy.Field(
		input_processor=MapCompose(remove_tags, filter_price),
		output_processor=TakeFirst(),
	)

# [cmd]
# from scrapy.loader import ItemLoader
# il = ItemLoader(item=Product())
# il.add_value('name', ['Welcome to my', '<strong>website</strong>'])
# il.add_value('price', ['&euro;', '<span>1000</span>'])
# il.load_item()

# [log]
# {'name': 'Welcome to my website', 'price': '1000'}