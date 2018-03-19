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
        
        if question is not None:
            search_recipes = Recipe.objects.filter(name__contains=question)
            print(search_recipes)
            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            context['last_question'] = '?q=%s' % question
            context['recipes_list'] = search_recipes
            
            # current_page = Paginator(search_articles, 10)
            # 
            # page = request.GET.get('page')
            # try:
            #     context['recipe_lists'] = current_page.page(page)
            # except PageNotAnInteger:
            #     context['recipe_lists'] = current_page.page(1)
            # except EmptyPage:
            #     context['recipe_lists'] = current_page.page(current_page.num_pages)

        return render_to_response(template_name=self.template_name, context=context)

