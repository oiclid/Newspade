from dynamic_scraper.spiders.django_checker import DjangoChecker
from  mysites.models import BBCNews, ReutersNews, AljazeeraNews


class NewsChecker(DjangoChecker):
	'''
	The JobChecker class inherits from the DjangoChecker class in the Dynamic Django scraper
	module hence why we imported it. The main aim of this module is checking the objects that we
	scrape mainly through the ref_object.url and see if there is any recurrence in the process. If 
	there is a recurrence the new object will be deleted to keep the integrity of the data. We will 
	also	configure a scheduler_runtime which will configure times at which the checker class will be run. 
	This is important especially after scheduling various cron jobs at which the scraper will be run.
	'''
	name = 'news_checker'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(BBCNews, **kwargs)
		self.scraper = self.ref_object.news_website.scraper
		self.scheduler_runtime = self.ref_object.checker_runtime
		super(NewsChecker, self).__init__(self, *args, **kwargs)

class ReutersChecker(DjangoChecker):
	'''
	The ReutersChecker class inherits from the DjangoChecker class in the Dynamic Django scraper
	module hence why we imported it. The main aim of this module is checking the objects that we
	scrape mainly through the ref_object.url and see if there is any recurrence in the process. If 
	there is a recurrence the new object will be deleted to keep the integrity of the data. We will 
	also	configure a scheduler_runtime which will configure times at which the checker class will be run. 
	This is important especially after scheduling various cron jobs at which the scraper will be run.
	'''
	name = 'Reuters_checker'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(ReutersNews, **kwargs)
		self.scraper = self.ref_object.reuters_website.scraper
		self.scheduler_runtime = self.ref_object.checker_runtime
		super(ReutersChecker, self).__init__(self, *args, **kwarg)

class AljazeeraChecker(DjangoChecker):
	'''
	The Aljazeera class inherits from the DjangoChecker class in the Dynamic Django scraper
	module hence why we imported it. The main aim of this module is checking the objects that we
	scrape mainly through the ref_object.url and see if there is any recurrence in the process. If 
	there is a recurrence the new object will be deleted to keep the integrity of the data. We will 
	also	configure a scheduler_runtime which will configure times at which the checker class will be run. 
	This is important especially after scheduling various cron jobs at which the scraper will be run.
	'''
	name = 'Aljazeera_checker'

	def __init__(self, *args, **kwargs):
		self._set_ref_object(AljazeeraNews, **kwargs)
		self.scraper = self.ref_object.aljazeera_website.scraper
		self.scheduler_runtime = self.ref_object.checker_runtime
		super(AljazeeraChecker, self).__init__(self, *args, **kwarg)
