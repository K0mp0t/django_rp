from . import soup

def custom_proc(request):
    if request.method == 'POST' and request.is_ajax:
        city = request.POST.get('city')
        weath_tuple = soup.weath(city)
        temperature = weath_tuple[0]
        conditions = weath_tuple[1]
    return {
        'temperature': temperature,
        'conditions': conditions,
    }