import datetime
from haystack import indexes
from .models import ReutersNews, BBCNews, AljazeeraNews, PoliticoNews
from articles.models import Articles

class NewsAdIndex(indexes.SearchIndex, indexes.Indexable):
	'''
	In this case we are creating a search index basesd in the django models
	of JobAd. Why JobAd? because that is where all the new jobs that we have 
	scraped are stored. In this way anybody can search for a particular job and
	get a good estimate result. It inherits from haystack indexes and from the 
	class SearchIndex and Indexable, gets the relevant model and returns then 
	JobAd.
	'''
	
	text = indexes.CharField(document=True, use_template=True, template_name="search/indexes/mysites/jobad_text.txt")
	title = indexes.CharField(model_attr='title')
	description = indexes.CharField(model_attr='description')
	url = indexes.CharField(model_attr='url')

	def get_model(self):
		return BBCNews

class ReutersAdIndex(indexes.SearchIndex, indexes.Indexable):
	'''
	In this case we are creating a search index basesd in the django models
	of JobAd. Why JobAd? because that is where all the new jobs that we have 
	scraped are stored. In this way anybody can search for a particular job and
	get a good estimate result. It inherits from haystack indexes and from the 
	class SearchIndex and Indexable, gets the relevant model and returns then 
	JobAd.
	'''
	
	text = indexes.CharField(document=True, use_template=True, template_name="search/indexes/mysites/jobad_text.txt")
	title = indexes.CharField(model_attr='title')
	description = indexes.CharField(model_attr='description')
	url = indexes.CharField(model_attr='url')
	

	def get_model(self):
		return ReutersNews

class AljazeeraAdIndex(indexes.SearchIndex, indexes.Indexable):
	'''
	In this case we are creating a search index basesd in the django models
	of JobAd. Why JobAd? because that is where all the new jobs that we have 
	scraped are stored. In this way anybody can search for a particular job and
	get a good estimate result. It inherits from haystack indexes and from the 
	class SearchIndex and Indexable, gets the relevant model and returns then 
	JobAd.
	'''
	
	text = indexes.CharField(document=True, use_template=True, template_name="search/indexes/mysites/jobad_text.txt")
	title = indexes.CharField(model_attr='title')
	description = indexes.CharField(model_attr='description')
	url = indexes.CharField(model_attr='url')

	def get_model(self):
		return AljazeeraNews

class PoliticoAdIndex(indexes.SearchIndex, indexes.Indexable):
	'''
	In this case we are creating a search index basesd in the django models
	of JobAd. Why JobAd? because that is where all the new jobs that we have 
	scraped are stored. In this way anybody can search for a particular job and
	get a good estimate result. It inherits from haystack indexes and from the 
	class SearchIndex and Indexable, gets the relevant model and returns then 
	JobAd.
	'''
	
	text = indexes.CharField(document=True, use_template=True, template_name="search/indexes/mysites/jobad_text.txt")
	title = indexes.CharField(model_attr='title')
	description = indexes.CharField(model_attr='description')
	url = indexes.CharField(model_attr='url')

	def get_model(self):
		return PoliticoNews

# class Articles(indexes.SearchIndex, indexes.Indexable):
# 	'''
# 	In this case we are creating a search index basesd in the django models
# 	of JobAd. Why JobAd? because that is where all the new jobs that we have 
# 	scraped are stored. In this way anybody can search for a particular job and
# 	get a good estimate result. It inherits from haystack indexes and from the 
# 	class SearchIndex and Indexable, gets the relevant model and returns then 
# 	JobAd.
# 	'''
	
# 	text = indexes.CharField(document=True, use_template=True, template_name="search/indexes/mysites/jobad_text.txt")
# 	title = indexes.CharField(model_attr='title')
# 	description = indexes.CharField(model_attr='description')
# 	url = indexes.CharField(model_attr='url')

# 	def get_model(self):
# 		return AljazeeraNews