from django import forms
from .models import GroceryItem

class GroceryForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = ['text_description']

    text_description = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Grocery Item'}))
