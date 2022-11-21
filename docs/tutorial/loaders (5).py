from itemloaders.processors import MapCompose
from myproject.ItemLoaders import ProductLoader

def strip_dashes(x):
	return x.strip('-')

class SiteSpecificLoader(ProductLoader):
	name_in = MapCompose(strip_dashes, ProductLoader.name_in)
