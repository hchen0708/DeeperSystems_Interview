from __future__ import unicode_literals


from django.db import models
from posts.models import Post

# Create your models here.


class Comment(models.Model):
	author = models.CharField(max_length=120, null=False, blank=False)
	comment_content = models.TextField(max_length=5000, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	parent = models.ForeignKey(Post, null=True, blank=True)
