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
	return render(request, 'landing/home.html', locals())
	