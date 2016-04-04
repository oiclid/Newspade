'''
'''
import json

from django.views.generic import ListView
from django.views.generic import DetailView

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, Http404, HttpResponseRedirect, get_object_or_404
from django.shortcuts import render_to_response, HttpResponse

from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.contrib.auth import get_user_model

from django_comments.views.moderation import perform_delete
from django_comments.models import Comment

# Create your views here.
from .models import Articles, Vote, ArticleVoteCountManager
from .forms import ArticleForm, VoteForm

user = get_user_model()

class HomeViews(ListView):
	'''
	This will be the home page of the project that will generate all the submitted articles
	from the users. It will generally inherit from Django Generic ListView and plan to
	implement a 25 object pagination. The queryset in this particular view will come from the 
	model manager with_votes which orders the objects/articles based on their votes.
	template_name = "home.html" 
	'''
	template_name = 'home.html'
	model = Articles
	queryset = Articles.with_votes.all()
	paginate_by = 25
	
	def get_context_data(self, **kwargs):

		context=super(HomeViews, self).get_context_data(**kwargs)
		
		if self.request.user.is_authenticated():

			voted = Vote.objects.filter(voter=self.request.user)
			articles_in_page = [article.id for article in context["articles_list"]]
			voted = voted.filter(article_id__in=articles_in_page)
			# change the objects to a list of numbers.
			voted = voted.values_list('article_id', flat=True)
			context["voted"] = voted

		return context
	

def single_view(request, slug):
	''' 
	this is a single_view of each article baser on the unique slug property which is 
	generated from the title of each individual article. 
	it takes in the following properties
	slug: unique article identifier generated from the article title
	if it cannot find the identifier or an article with the identifier, it will raiser
	a 404 error.
	else
	it will return the 
	template_name: single.html
	context: a dict with the queried objects and the association with what it will be called
	on the template.
	'''
	try:
		articles = Articles.objects.get(slug=slug)
		context = {'single_article':articles}	
		template_name="articles/single.html"
		return render(request, template_name, context)
	except:
		raise Http404





class UpdateArticle(UpdateView):
	'''
	This is an update article view which will inherit from the generic class based UpdateView 
	django provides. Its main aim is to give users a chance to update their own articles and 
	and give them a chance to make corrections because lets face it "humans is to error."

	'''
	model = Articles
	fields=['title', 'content', 'banner', 'tags', 'tldr' ]
	
	
	template_name = "forms/forms.html"

class ArticleDeletion(DeleteView):
	'''
	this is an article delete option view. The plan is to delete each individual article based
	on the user who submitter it.
	'''
	model = Articles
	success_url = reverse_lazy("logs")


@login_required
def article_form_view(request):
	'''
	this is based from the forms for the submitted user articles from forms.py. Similar form 
	processing logic thst each developer knows including processing pictures for the banner
	that could be placed at the very top of each article. 
	'''
	
	btn = 'submit'
	if request.method == "POST":
		

		form = ArticleForm(request.POST or None, request.FILES or None )
		
		if form.is_valid():

			new_article = form.save(commit=False)			
			new_article.submitter =request.user
			new_article.total_score = 0.0
			new_article.save()
			
			
		return HttpResponseRedirect('/logs')
	else:
		form = ArticleForm()
		

	template_name = "articles/forms.html"
	context = {
	"form":form,	
	"submit_btn": btn,
	}
	return render(request, template_name, context)

def delete_own_comment(request, id):
	'''
	here we will allow users to delete their own comments based on the 
	logic that if they submitted it they should be able to take it delete_own_comment
	this view takes in
	id: the comment id that was submitted by the user now up for review and deletion
	by the user
	'''
	comment = get_object_or_404(Comment, id=id)
	if comment.user.id != request.user.id:
		raise Http404
	perform_delete(request, comment)
	return HttpResponseRedirect(comment.content_object.get_absolute_url())



class JsonFormMixin(object):

	def create_response(self, vdict=dict(), valid_form=True):
		response = HttpResponse(json.dumps(vdict),
		 content_type='application/json')
		response.status = 200 if valid_form else 500
		return response


class VoteFormBaseView(FormView):
	form_class = VoteForm

	def create_response(self, vdict=dict(), valid_form=True):
		response = HttpResponse(json.dumps(vdict),
		 content_type='application/json')
		response.status = 200 if valid_form else 500
		return response

	def form_valid(self, form):
		article = get_object_or_404(Articles, pk=form.data["article"])
		user = self.request.user
		prev_votes = Vote.objects.filter(voter=user, article=article)
		has_voted = (len(prev_votes) > 0)
		ret = {"success": 1}

		if not has_voted:
			v = Vote.objects.create(voter=user, article=article)
			ret["voteobj"] = v.id
			
			# return HttpResponseRedirect("/")
		else:
			prev_votes[0].delete()
			ret["unvoted"] = 1
			
		return self.create_response(ret, True)
		

	def form_invalid(self, form):
		ret = {"success" : 0, "form_errors":form.errors}
		return self.create_response(ret, False)


class VoteFormView(JsonFormMixin, VoteFormBaseView):
	pass

def tag_page(request, tag):
	'''
	tag: the tag object that the user provides when submitting an article
	'''
	article = Articles.objects.filter(tags__name=tag)
	template_name="articles/tags.html"
	context = {"article":article, 
				"tag":tag,
				}
	return render(request, template_name, context)

def about(request):
	template_name="articles/about.html"
	return render(request, template_name)
def custom_404(request):
	template_name="404.html"
	return render_to_response(template_name)
def custom_400(request):
	template_name="400.html"
	return render_to_response(template_name)
def custom_500(request):
	template_name="500.html"
	return render_to_response(template_name)