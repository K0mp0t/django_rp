from django.shortcuts import render
from .forms import VisitorForm

def landing(request):
	
	form = VisitorForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		data = form.cleaned_data
		print (data['name'])
		new_form = form.save()
	return render(request, 'landing/landing.html', locals())
	