# from django.shortcuts import render
# 
# def search(request):
#     
#     return render(request, 'search/search.html', locals())

from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View

from recipes.models import Recipe


class ESearchView(View):
    template_name = 'search/search.html'

    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        question = question.lower()
        
        if question is not None:
            search_recipes = Recipe.objects.filter(name__contains=question[1:])
            context['last_question'] = '?q=%s' % question
            context['recipes_list'] = search_recipes

        return render_to_response(template_name=self.template_name, context=context)

