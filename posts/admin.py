from django.contrib import admin
from .models import Post
from django.utils.text import slugify

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'timestamp']
	prepopulated_fields = {'slug': ["title"]}

	class Meta:
		model = Post


admin.site.register(Post, PostAdmin)
