from django.contrib import admin
from .models import *

class RecipeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Recipe._meta.fields]
    
    class Meta:
        model = Recipe
        
admin.site.register(Recipe, RecipeAdmin)





