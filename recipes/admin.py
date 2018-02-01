from django.contrib import admin
from .models import *

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 0
    
class RecipeTagInline(admin.TabularInline):
    model = RecipeTag
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Recipe._meta.fields]
    inlines = [RecipeImageInline, RecipeTagInline]
    
    class Meta:
        model = Recipe
        
admin.site.register(Recipe, RecipeAdmin)

class RecipeImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RecipeImage._meta.fields]
    
    class Meta:
        model = RecipeImage
        
admin.site.register(RecipeImage, RecipeImageAdmin)

class RecipeTagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RecipeTag._meta.fields]
    
    class Meta:
        model = RecipeTag
        
admin.site.register(RecipeTag, RecipeTagAdmin)



