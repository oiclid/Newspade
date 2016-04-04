from django.test import TestCase
from django.template.defaultfilters import slugify
# Create your tests here.
from .models import Articles

class ArticlesModelTest(TestCase):

	def test_string_rep(self):
		article = Articles(title= "the test title")
		self.assertEqual(str(article), article.title)

	def test_homepage(self):
		'''
		Testing to make sure that the url is working. This is where the home page
		will be held
		'''

		response = self.client.get("/")
		self.assertEqual(response.status_code, 200)

	# def test_get_absolute_url(self):
	# 	articles = Articles.objects.create(title= "the test title")
	# 	self.assertIsNotNone(articles.get_absolute_url())

class HomepageTest(TestCase):
	'''
	we are going to test whether the blog entries show up on the
	homepage
	'''

	def test_one_entry(self):
		Articles.objects.create(title="title-1", content="content-1")
		response = self.client.get('/')
		self.assertContains(response, 'title-1')
		self.assertContains(response, 'content-1')

	
class ArticleViewTest(TestCase):
	"passed this test"

	def set_up(self):
		self.articles = Articles.objects.create(title='extreme situation', content="content-1")
		self.slug = slugify(title)
	def single_article_test(self):
		url  = "articles/{slug}"
		response=self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, template_name='articles/single.html')
