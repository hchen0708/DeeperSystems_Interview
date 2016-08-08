from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^create/$', views.post_create),
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),
    
]