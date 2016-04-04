from django.contrib import admin

# Register your models here.
from .models import Articles, Vote

class ArticleAdmin(admin.ModelAdmin):
	list_display = ("__str__", "timestamp", "updated", "active", "featured")

	prepopulated_fields = {"slug":("title",)}

class VoteAdmin(admin.ModelAdmin):
	pass

admin.site.register(Articles, ArticleAdmin)
admin.site.register(Vote,VoteAdmin)

