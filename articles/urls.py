from django.contrib import admin
from django.conf.urls import url
from . import views
from django.urls import re_path

app_name = 'articles'

urlpatterns=[
    url(r'^$',views.articles_home,name='articles_home'),
    url(r'^news',views.news,name='news'),
    url(r'^transfers',views.transfers,name='transfers'),
    url(r'^analysis',views.analysis,name='analysis'),
    url(r'^create/$',views.create,name='create'),
    re_path('(?P<slug>[\w-]+)/$', views.article_detail,name='detail')
]
