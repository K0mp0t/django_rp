from django.shortcuts import render
from recipes.models import *

def recipe(request, recipe_id):
    
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/recipes.html', locals())
