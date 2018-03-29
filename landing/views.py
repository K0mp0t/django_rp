from django.shortcuts import render
from .forms import VisitorForm
from recipes.models import Recipe

def home(request):
	recipes = Recipe.objects.all()
	for recipe in recipes:
		recipe.status = 'Архив'
		recipe.save(update_fields=['status'])
	k = 0
	recipes = Recipe.objects.order_by('-created')
	for i in range(9):
		recipe_new = recipes[0+k]
		recipe_new.status = 'Свежее'
		recipe_new.save(update_fields=['status'])
		k += 1
	recipes = Recipe.objects.order_by('-views_counter')
	k = 0
	for i in range(6):
		recipe_best = recipes[0+k]
		if recipe_best.status != 'Свежее':
			recipe_best.status = 'Лучшее'
			recipe_best.save(update_fields=['status'])
			k += 1
	recipes_new = Recipe.objects.filter(status='Свежее')
	# recipes_hot = Recipe.objects.filter(status='Популярное')
	recipes_best = Recipe.objects.filter(status='Лучшее')
	return render(request, 'landing/home.html', locals())
	
def new(request):
	
	# recipes = Recipe.objects.all()
	# for recipe in recipes:
	# 	recipe.status = 'Архив'
	# 	recipe.save(update_fields=['status'])
	# k = 0
	# recipes = Recipe.objects.order_by('created')
	# for i in range(2):
	# 	recipe_new = recipes[0+k]
	# 	recipe_new.status = 'Свежее'
	# 	recipe_new.save(update_fields=['status'])
	# 	k += 1
	recipes_new = Recipe.objects.filter(status='Свежее')
	return render(request, 'recipes/new.html', locals())

def best(request):
	
	# recipes = Recipe.objects.all()
	# for recipe in recipes:
	# 	recipe.status = 'Архив'
	# 	recipe.save(update_fields=['status'])
	# recipes = Recipe.objects.order_by('-views_counter')
	# k = 0
	# for i in range(1):
	# 	recipe_best = recipes[0+k]
	# 	recipe_best.status = 'Лучшее'
	# 	recipe_best.save(update_fields=['status'])
	# 	k += 1
	recipes_best = Recipe.objects.filter(status='Лучшее')
	return render(request, 'recipes/best.html', locals())

def archive(request):
	
	recipes_arc = Recipe.objects.filter(status='Архив')
	return render(request, 'recipes/archive.html', locals())

def hot(request):
	
	recipes = Recipe.objects.all()
	recipes_hot = Recipe.objects.filter(status='Популярное')
	return render(request, 'recipes/hot.html', locals())

def about(request):
	return render(request, 'landing/about.html', locals())
