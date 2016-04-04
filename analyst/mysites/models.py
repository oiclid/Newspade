from __future__ import unicode_literals


from django.db import models
from django.db.models.signals import pre_delete
from scrapy_djangoitem import DjangoItem
from dynamic_scraper.models import Scraper, SchedulerRuntime
from django.dispatch import receiver
# Create your models here.



class NewsWebsite(models.Model):
	'''
	in this situation this is the news website that we will be scraping from. So for instance if we are looking for all 
	the business analyst postions from indeed.com this particular django models wll specify what website is nessecary for
	which particular Article. 
	It borrows from thenm django class models.Model to do the job.
	The scraper variable is the actual scraper that will borrow from the dynamic_scraper modules and is responsible 
	for using scrapy functions to scrape whatever website we desire.
	The scraper_runtime is as the title suggest. It borrows from the SchedulerRuntime class of the dynamic_scraper modulesd
	'''

	title = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)



class BBCNews(models.Model):
	'''
	This particular class is concerned with receiving all the scraped material once the job is done. For instance if we are scraping 
	business analyst positions from a company in mountain view then what we expect is that:
	title = "Donald Trump wins the Primaries only to be dumped by republicans"
	url = www.company.com/news.html (or something similar)
	description = Description|truncated.
	'''

	news_website = models.ForeignKey(NewsWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="BBC News", max_length=100)
	

	def __str__(self):
		return self.title
	
	class Meta:
		ordering = ['-id']
		verbose_name_plural = "BBCNews"



class NewsAdItem(DjangoItem):
	'''
	this is a scrapy requirement for all results in the scrapy instance to be saved in the sqlite/Postgresql database in the 
	django database.
	'''

	django_model = BBCNews


class ReutersWebsite(models.Model):
	'''
	in this situation this is the news website that we will be scraping from. So for instance if we are looking for all 
	the business analyst postions from indeed.com this particular django models wll specify what website is nessecary for
	which particular Article. 
	It borrows from thenm django class models.Model to do the job.
	The scraper variable is the actual scraper that will borrow from the dynamic_scraper modules and is responsible 
	for using scrapy functions to scrape whatever website we desire.
	The scraper_runtime is as the title suggest. It borrows from the SchedulerRuntime class of the dynamic_scraper modulesd
	'''

	head = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)


class ReutersNews(models.Model):

	news_website = models.ForeignKey(ReutersWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="Reuters", max_length=100)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']
		verbose_name_plural = "ReutersNews"

class ReutersAdItem(DjangoItem):

	django_model = ReutersNews

class AljazeeraWebsite(models.Model):
	'''
	in this situation this is the news website that we will be scraping from. So for instance if we are looking for all 
	the business analyst postions from indeed.com this particular django models wll specify what website is nessecary for
	which particular Article. 
	It borrows from thenm django class models.Model to do the job.
	The scraper variable is the actual scraper that will borrow from the dynamic_scraper modules and is responsible 
	for using scrapy functions to scrape whatever website we desire.
	The scraper_runtime is as the title suggest. It borrows from the SchedulerRuntime class of the dynamic_scraper modulesd
	'''

	head = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)


class AljazeeraNews(models.Model):

	news_website = models.ForeignKey(AljazeeraWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="Aljazeera", max_length=100)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']
		verbose_name_plural = "AljazeeraNews"

class AljazeeraAdItem(DjangoItem):

	django_model = AljazeeraNews

class PoliticoWebsite(models.Model):
	'''
	in this situation this is the news website that we will be scraping from. So for instance if we are looking for all 
	the business analyst postions from indeed.com this particular django models wll specify what website is nessecary for
	which particular Article. 
	It borrows from thenm django class models.Model to do the job.
	The scraper variable is the actual scraper that will borrow from the dynamic_scraper modules and is responsible 
	for using scrapy functions to scrape whatever website we desire.
	The scraper_runtime is as the title suggest. It borrows from the SchedulerRuntime class of the dynamic_scraper modulesd
	'''

	head = models.CharField(max_length=250)
	url = models.URLField()
	scraper = models.ForeignKey(Scraper, blank= True, null=True, on_delete=models.SET_NULL)
	scraper_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)


class PoliticoNews(models.Model):

	news_website = models.ForeignKey(PoliticoWebsite)
	checker_runtime = models.ForeignKey(SchedulerRuntime, blank= True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250)
	url = models.URLField()
	description = models.TextField(blank=True)
	date = models.DateTimeField(auto_now=True)
	company = models.CharField(default="Politico", max_length=100)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']
		verbose_name_plural = "Politico News"

class PoliticoAdItem(DjangoItem):

	django_model = PoliticoNews


@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
	if isinstance(instance, NewsWebsite):
		if instance.scraper_runtime:
			instance.scraper_runtime.delete()
	
	if isinstance(instance, BBCNews):
		if instance.checker_runtime:
			instance.checker_runtime.delete()

pre_delete.connect(pre_delete_handler)
