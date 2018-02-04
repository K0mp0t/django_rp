from django.db import models
import datetime

class Recipe(models.Model):
    TAG_CHOICES = (('H', 'Горячее блюдо'), ('C', 'Холодное блюдо'), ('Salad', 'Салат'), ('Soup', 'Суп'), ('Bakery', 'Выпечка'))
    
    name = models.CharField(max_length=64, default=None)
    description = models.TextField(default=None)
    full_recipe = models.TextField(default=None)
    tag = models.CharField(max_length=64, choices=TAG_CHOICES, default=None)
    image = models.ImageField(upload_to='media/recipes/images/', blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return 'Рецепт %s' % self.name
    
    class Meta:
        verbose_name='Рецепт'
        verbose_name_plural='Рецепты'
        

        
