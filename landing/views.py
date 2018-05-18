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
	try:
		for i in range(9):
			recipe_new = recipes[0+k]
			recipe_new.status = 'Свежее'
			recipe_new.save(update_fields=['status'])
			k += 1
		k = 0
		recipes = Recipe.objects.order_by('-views_counter')
		i = 0
		while i < 6:
			recipe_best = recipes[0+k]
			if recipe_best.status != 'Свежее':
				recipe_best.status = 'Лучшее'
				recipe_best.save(update_fields=['status'])
				i += 1
			k += 1
		k = 0

	except IndexError:
		pass
	recipes_new = Recipe.objects.filter(status='Свежее')
	# recipes_hot = Recipe.objects.filter(status='Популярное')
	recipes_best = Recipe.objects.filter(status='Лучшее')
	return render(request, 'landing/home.html', locals())
	
def new(request):
	
	recipes_new = Recipe.objects.filter(status='Свежее')
	return render(request, 'recipes/new.html', locals())

def best(request):
	
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

def tags(request):
	pokushatz = request.GET.get('pokushatz')
	recipes = Recipe.objects.filter(tag=pokushatz)
	if pokushatz == 'Суп':
		header = 'Супы'
	if pokushatz == 'Салат':
		header = 'Салаты'
	if pokushatz == 'Горячее блюдо':
		header = 'Горячие блюда'
	if pokushatz == 'Холодное блюдо':
		header = 'Холодные блюда'
	if pokushatz == 'Выпечка':
		header = 'Выпечка'
	return render(request, 'landing/pokushatz.html', locals())
	

