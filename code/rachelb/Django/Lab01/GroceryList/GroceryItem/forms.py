from django import forms 
from django.forms import ModelForm
from .models import * 


class GroceryItemsForm(forms.ModelForm):
    class Meta:
        model = GroceryItems
        fields = '__all__'