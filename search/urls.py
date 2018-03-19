from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'search'

urlpatterns = [
	url(r'^search/$', views.ESearchView.as_view(), name = 'index'),
]