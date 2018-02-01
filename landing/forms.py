from django import forms
from .models import *

class VisitorForm(forms.ModelForm):
    
    class Meta:
        model = visitor
        exclude = ['']