from __future__ import unicode_literals

from dynamic_scraper.spiders.django_spider import DjangoSpider
from mysites.models import BBCNews, NewsWebsite, NewsAdItem 
from mysites.models import ReutersNews, ReutersWebsite, ReutersAdItem
from mysites.models import AljazeeraNews, AljazeeraWebsite, AljazeeraAdItem
from mysites.models import PoliticoNews, PoliticoWebsite, PoliticoAdItem

class NewsSpider(DjangoSpider):

	name = 'news_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(NewsWebsite, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = BBCNews
		self.scraped_obj_item_class = NewsAdItem
		super(NewsSpider, self).__init__(self, *args, **kwargs)

class ReuterSpider(DjangoSpider):

	name = 'reuters_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(ReutersWebsite, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = ReutersNews
		self.scraped_obj_item_class = ReutersAdItem
		super(ReuterSpider, self).__init__(self, *args, **kwargs)

class AljazeeraSpider(DjangoSpider):

	name = 'aljazeera_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(AljazeeraWebsite, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = AljazeeraNews
		self.scraped_obj_item_class = AljazeeraAdItem
		super(AljazeeraSpider, self).__init__(self, *args, **kwargs)

class PoliticoSpider(DjangoSpider):

	name = 'politico_spider'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(PoliticoWebsite, **kwargs)
		self.scraper = self.ref_object.scraper
		self.scrape_url = self.ref_object.url
		self.scheduler_runtime = self.ref_object.scraper_runtime
		self.scraped_obj_class = PoliticoNews
		self.scraped_obj_item_class = PoliticoAdItem
		super(PoliticoSpider, self).__init__(self, *args, **kwargs)