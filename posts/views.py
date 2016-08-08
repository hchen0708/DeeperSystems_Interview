from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify

from .models import Post
from comments.models import Comment
from .forms import PostForm
from comments.forms import CommentForm
# Create your views here.


def post_list(request):
	queryset = Post.objects.all().order_by("-timestamp")
	context = {
		"object_list": queryset,
		"title": "List",

	}
	return render(request, "list.html", context)

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.slug = slugify(form.cleaned_data.get('title'))
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form": form,
	}
	return render(request, "create.html", context)


def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)

	comments = Comment.objects.filter(parent=instance.id)
	
	init_data = {
		"parent": instance.id
	}

	form = CommentForm(request.POST or None, initial=init_data)
	if form.is_valid():
		ins = form.save(commit=False)
		ins.save()



	context = {
		"title": instance.title,
		"instance": instance,
		"comments": comments,
		"form": form,

	}
	return render(request, "detail.html", context)
