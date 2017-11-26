from django.shortcuts import render
from django.http import HttpResponse
import json
from . import soup

def weather(request):
    if request.method == 'POST' and request.is_ajax:
        city = request.POST.get("city")
        weath_tuple = soup.weath(city)
        temperature = weath_tuple[0]
        conditions = weath_tuple[1]
        response_dict = {'temperature': temperature, 'conditions': conditions}
        return HttpResponse(json.dumps(response_dict), content_type='application/json')
    if request.method == 'GET':
        return render(request, 'weather/weather.html')