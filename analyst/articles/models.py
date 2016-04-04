'''
This will be the model that will be hold all the user submitted articles which will eventually
be shown on the frontpage of the site. In this particular models, the plan is to implement a 
model that has all the information nessecary needed to make a coherent and fast article to grasp.
Responsibilities of this particular page include but are not limited to:
1) Models that hold the articles.
2) The relationship between the votes that a user submits, the user himself, and the article
to receive the vote.
3)A rudimentary vote and ranking algorithm that will be asynchronously implemented by Celery
    - this will be named "set_rank" and is bound to be run each hour to generate a new post 
    based on the number of upvotes given to a specific post.

'''
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Count

from django.db.models.signals import post_save
from django.utils.timezone import now
from markdownx.models import MarkdownxField
from taggit.managers import TaggableManager

# Create your models here.

class ArticleVoteCountManager(models.Manager):
	def get_queryset(self):
		return super(ArticleVoteCountManager, self).get_queryset().annotate(
			votes=Count('vote')).order_by('-total_score', '-votes')

class Articles(models.Model):
	title = models.CharField(max_length=140, blank =False, null=False)
	submitter = models.ForeignKey(User)
	banner = models.ImageField(upload_to='media/pics', null=True,blank=True)
	content = MarkdownxField(max_length=100000, blank=False, null=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	tldr= MarkdownxField("TLDR;", null=True,blank=True)
	active = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	slug = models.SlugField(unique=True)
	total_score = models.FloatField(default=0.0)
	with_votes = ArticleVoteCountManager()
	objects = models.Manager()
	tags = TaggableManager()


	def __str__(self):
		return self.title

	class Meta:
		unique_together = ("title", "slug",)
		

	def get_absolute_url(self):
		return reverse('single_view', kwargs={'slug':self.slug})

	def set_rank(self):
		SECS = float(60*60)
		GRAVITY = 1.2

		delta = now() - self.timestamp
		item_hour_age = delta.total_seconds()
		votes = self.votes-1 # remove the users own vote from the equation
		self.total_score = votes / pow((item_hour_age), GRAVITY)
		self.save()


class Vote(models.Model):
	voter = models.ForeignKey(User)
	article = models.ForeignKey(Articles)
	def __unicode__(self):
		return "%s upvoted %s" %(self.voter.username, self.article.title)






	
