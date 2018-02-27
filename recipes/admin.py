from django.contrib import admin
from .models import *

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'views_counter', 'tag', 'status', 'image', 'created', 'updated']
    
    class Meta:
        model = Recipe
        
admin.site.register(Recipe, RecipeAdmin)





