from django import forms

from django.utils.text import slugify
from .models import Articles, Vote
from markdown_deux.templatetags.markdown_deux_tags import markdown_allowed
from django.core.files.images import get_image_dimensions
class ArticleForm(forms.ModelForm):
	content = forms.CharField(
		label="content (required)",
		widget=forms.Textarea(attrs={"size":40}),
		required=True),

	class Meta:
		model = Articles
		fields = ['title', 'content', 'tags', 'tldr']
		exclude = ("user", "total_score")

	def clean_title(self):
		title = self.cleaned_data.get("title")
		return title

	def clean_content(self):
		content = self.cleaned_data.get("content")
		return content

	def clean_picture(self):
		banner = self.cleaned_data.get("banner")
		
		try:
			w,h = get_image_dimensions(banner)

			max_width=900
			max_height = 300

			if w>max_width or h>max_height:
				raise forms.ValidationError(
					u'please use an image smaller than that'
					)
			# validate the content type
			main, sub = banner.content_type.split('/')

			if not(main=='image' and sub in ['jpg', 'jpeg', 'gif','png']):
				raise forms.ValidationError(u'please use a JPEG, GIF or PNG')

			if len(banner)> (20*1024):
				raise forms.ValidationError(
					"picture size may not exceed 20k.")
		except AttributeError:
			pass

		return banner
	def clean_tags(self):
		tags = self.cleaned_data.get("tags")
		return tags

	def save(self, commit=True):		
		article = super(ArticleForm, self).save(commit=False)
		article.slug = slugify(article.title)
		# article.submitter = self.request.user
		if commit:
			article.save()

		return article

class VoteForm(forms.ModelForm):

	class Meta:
		model = Vote
		exclude = ("voter",)