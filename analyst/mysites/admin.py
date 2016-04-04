from __future__ import unicode_literals
from django.contrib import admin
from .models import BBCNews, NewsWebsite, ReutersNews, ReutersWebsite
from .models import AljazeeraNews, AljazeeraWebsite
from .models import PoliticoNews, PoliticoWebsite

class NewsWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'url_', 'scraper',)
	list_display_links = ('title',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class NewsAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_','company')
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)

	def url_(self, instance):

		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)
	url_.allow_tags = True



class ReutersWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'head', 'url_', 'scraper',)
	list_display_links = ('head',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class ReutersAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_','company')
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)
	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url, title=instance.url)

	url_.allow_tags = True
class AljazeeraWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'head', 'url_', 'scraper',)
	list_display_links = ('head',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class AljazeeraAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_',)
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)
	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url, title=instance.url)

	url_.allow_tags = True

class PoliticoWebsiteAdmin(admin.ModelAdmin):
	list_display = ('id', 'head', 'url_', 'scraper',)
	list_display_links = ('head',)

	def url_(self, instance):
		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)

	url_.allow_tags = True

class PoliticoAdAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date','url_','company')
	list_display_links = ('title',)
	raw_id_fields = ('checker_runtime',)

	def url_(self, instance):

		return '<a href="{url}" target="_blank">{title}</a>'.format(
			url=instance.url,title=instance.url)
	url_.allow_tags = True



admin.site.register(NewsWebsite, NewsWebsiteAdmin)
admin.site.register(BBCNews, NewsAdAdmin)

admin.site.register(ReutersWebsite, ReutersWebsiteAdmin)
admin.site.register(ReutersNews, ReutersAdAdmin)

admin.site.register(AljazeeraWebsite, AljazeeraWebsiteAdmin)
admin.site.register(AljazeeraNews, AljazeeraAdAdmin)

admin.site.register(PoliticoWebsite, PoliticoWebsiteAdmin)
admin.site.register(PoliticoNews, PoliticoAdAdmin)