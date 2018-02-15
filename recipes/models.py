from django.db import models
import datetime

class Recipe(models.Model):
    TAG_CHOICES = (('Горячее блюдо', 'Горячее блюдо'), ('Холодное блюдо', 'Холодное блюдо'), ('Салат', 'Салат'), ('Суп', 'Суп'), ('Выпечка', 'Выпечка'))
    STATUS_CHOICES = (('Свежее', 'Свежее'), ('Популярное', 'Популярное'), ('Лучшее', 'Лучшее')) 
    
    name = models.CharField(max_length=64, default=None)
    description = models.TextField(default=None)
    ingredients = models.TextField(default=None)
    full_recipe = models.TextField(default=None)
    tag = models.CharField(max_length=64, choices=TAG_CHOICES, default=None)
    status = models.CharField(max_length=64, choices=STATUS_CHOICES, default=None, blank=True, null=True)
    image = models.ImageField(upload_to='recipes/images/', blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return 'Рецепт %s' % self.name
    
    class Meta:
        verbose_name='Рецепт'
        verbose_name_plural='Рецепты'
        

        
