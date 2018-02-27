from django.shortcuts import render
from recipes.models import *
from django.db.models import Count

def recipe(request, recipe_id):
    
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.views_counter += 1
    recipe.save(update_fields=['views_counter'])
    recipes = Recipe.objects.order_by('-views_counter')
    k = 0
    while k < 2:
        recipe_best = recipes[0+k]
        recipe_best.status = 'Лучшее'
        recipe_best.save(update_fields=['status'])
        k += 1
    
    k = 0
    recipes = Recipe.objects.order_by('-created')
    while k < 1:
        recipe_new = recipes[0+k]
        recipe_best.status = 'Свежее'
        recipe_best.save(update_fields=['status'])
        k += 1
        
    return render(request, 'recipes/recipes.html', locals())
