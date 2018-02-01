from django.db import models
import datetime

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=64, default=None)
    recipe_description = models.TextField(default=None)
    full_recipe = models.TextField(default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return 'Рецепт %s' % self.recipe_name
    
    class Meta:
        verbose_name='Рецепт'
        verbose_name_plural='Рецепты'
        
class RecipeTag(models.Model):
    TAG_CHOICES = (('H', 'Горячее блюдо'), ('C', 'Холодное блюдо'), ('Salad', 'Салат'), ('Soup', 'Суп'), ('Bakery', 'Выпечка'))
    
    recipe = models.ForeignKey(Recipe, blank=True, null=True, default=None)
    recipe_tag = models.CharField(max_length=64, choices=TAG_CHOICES, default=None)
    
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        
class RecipeImage(models.Model):
    recipe = models.ForeignKey(Recipe, blank=True, null=True, default=None)
    recipe_image = models.ImageField(upload_to='media/recipes/images/')
    
    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        
