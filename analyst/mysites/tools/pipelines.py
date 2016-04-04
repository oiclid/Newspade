from __future__ import unicode_literals
from builtins import str, object

import logging
from scrapy.exceptions import DropItem

from django.db.utils import IntegrityError
from dynamic_scraper.models import SchedulerRuntime

class DjangoWriterPipeline(object):

	def process_item(self, item, spider):
		'''

		this is the processing portion of the spider to the django ORM/Database. What this particular
		portion does is that it gets the spider and based on the configuration it will save the 
		information in my DB. It follows the same rules and principles of the scrapy pipeline model. In 
		case there is an intgrity error, it will drop the items and give back and errot of missing attrib

		'''
		
		if spider.conf['DO_ACTION']:
			try:
				item['news_website'] = spider.ref_object

				checker_rt = SchedulerRuntime(runtime_type='C')
				checker_rt.save()
				item['checker_runtime'] = checker_rt
				item.save()
				spider.action_successful = True
				spider.log("Items saved in the DB", logging.INFO)

			except IntegrityError, e:
				spider.log(str(e), logging.ERROR)
				raise DropItem("missing attrib")
			
		
		return item
