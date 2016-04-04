from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	picture = models.ImageField( null=True, blank=True, upload_to='media/profile')
	bio = MarkdownxField(null=True)
	firstName = models.CharField("First Name", max_length=140, null=True, blank=True)
	lastName = models.CharField("Last Name", max_length=140, null=True, blank=True)
	jobtitle = models.CharField("Job Title", max_length=140, null=True, blank=True)
	age = models.IntegerField(default=18, null=True, blank=True)
	facebook = models.URLField("Facebook", null=True, blank=True)
	googleplus = models.URLField("Google +", null=True, blank=True)
	linkedin = models.URLField("LinkedIn", null=True, blank=True)
	twitter = models.URLField("Twitter", null=True, blank=True)

	def __unicode__(self):
		return "%s profile" %self.user

def create_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)

#lets save the user by signals

post_save.connect(create_profile, sender=User)