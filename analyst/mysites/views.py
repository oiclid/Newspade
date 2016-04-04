from django.shortcuts import render
from .models import BBCNews, ReutersNews, AljazeeraNews, PoliticoNews
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class NewsListAdView(ListView):
	# model = NewsAd

	queryset = BBCNews.objects.order_by( '-date')
	template_name = "news/bbc.html"
	paginate_by = 25
	context_object_name = "news"

	
class ReutersListAdView(ListView):
	# model = NewsAd

	queryset = ReutersNews.objects.order_by( '-date')
	template_name = "news/reuters.html"
	paginate_by = 25
	context_object_name = "news"

	

class AljazeeraListAdView(ListView):
	# model = NewsAd

	queryset = AljazeeraNews.objects.order_by("-date")
	template_name = "news/aljazeera.html"
	paginate_by = 25
	context_object_name = "news"

class PoliticoListAdView(ListView):
	# model = NewsAd

	queryset = PoliticoNews.objects.order_by("-date")
	template_name = "news/politico.html"
	paginate_by = 25
	context_object_name = "news"

	


	