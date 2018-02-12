from django.conf.urls import url, include
from django.contrib import admin
from recipes import views
from recipes.models import *

urlpatterns = [
	url(r'^recipes/(?P<recipe_id>\w+)/$', views.recipe, name = 'recipe'),
]