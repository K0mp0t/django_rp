from django.contrib import admin
from .models import *

class visitorAdmin (admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    exclude = ['email']
    list_filter = ['name']
    search_fields = ['name', 'email', 'id']
    
    class Meta:
        model = visitor

admin.site.register(visitor, visitorAdmin)

