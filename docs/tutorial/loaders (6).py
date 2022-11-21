from itemloaders.processors import MapCompose
from myproject.ItemLoaders import ProductLoader
from myproject.utils.xml import remove_cdata

class XmlProductLoader(ProductLoader):
	name_in = MapCompose(remove_cdata, ProductLoader.name_in)
