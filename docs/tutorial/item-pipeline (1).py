# 가격 확인 및 가격 없는 항목 삭제

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
class PricePipeline:

	vat_factor = 1.15

	def process_item(self, item, spider):
		adapter = ItemAdapter(item)
		if adapter.get('price'):
			if adapter.get('price_excludes_vat'):
				adapter['price'] = adapter['price'] * self.vat_factor
			return item
		else:
			raise DropItem(f"Missing price in {item}")