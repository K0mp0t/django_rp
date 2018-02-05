from django.shortcuts import render
from .forms import VisitorForm
from recipes.models import Recipe

def landing(request):
	
	form = VisitorForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		data = form.cleaned_data
		print (data['name'])
		new_form = form.save()
		
	return render(request, 'landing/landing.html', locals())

def home(request):
	recipes = Recipe.objects.all()
	recipes_new = Recipe.objects.filter(status='Свежее')
	recipes_hot = Recipe.objects.filter(status='Популярное')
	recipes_best = Recipe.objects.filter(status='Лучшее')
	return render(request, 'landing/home.html', locals())
	