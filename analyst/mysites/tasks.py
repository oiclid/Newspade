from celery.task import task
from django.db.models import Q
from dynamic_scraper.utils.task_utils import TaskUtils
from .models import BBCNews, NewsWebsite

@task
def run_spiders():
	t = TaskUtils()
	# Django field lookup keyword arguments to specify which ref objects(JobWebsite)
	# to run
	kwargs = {
		'scrape_me':True,
	}
	args=(Q(name = 'BBC'),)
	t.run_spiders(NewsWebsite, 'scraper', 'scraper_runtime', 'news_spider', *args, **kwargs)
	
@task
def run_checkers():
	t = TaskUtils()

	kwargs = {
		'check_me':True,
	}
	args=(Q(id__gt = 100),)
	t.run_checkers(BBCNews, 'news_website__scraper', checker_runtime, 'news_checker', *args, **kwargs)
