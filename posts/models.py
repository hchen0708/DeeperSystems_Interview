from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from django.core.urlresolvers import reverse
# Create your models here.

class PostManager(models.Manager):
	def all(self):
		return super(PostManager, self).filter(publish__lte=timezone.now())	

class Post(models.Model):
	author = models.CharField(max_length=120, null=False, blank=False)
	title = models.CharField(max_length=500, null=False, blank=False)
	post_content = models.TextField(max_length=5000, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return "%s - %s" % (self.title, self.author)

	def get_absolute_url(self):
		return reverse("detail", kwargs={"slug": self.slug})
