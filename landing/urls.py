from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^recipes/$', views.home, name = 'home'),
	url(r'^$', views.home, name = 'home'),
	url(r'^recipes/new/$', views.new, name = 'new'),
	url(r'^recipes/best/$', views.best, name = 'best'),
	url(r'^recipes/hot/$', views.hot, name = 'hot'),
	url(r'^recipes/archive/$', views.archive, name = 'archive'),
	url(r'^about/$', views.about, name = 'about'),
]