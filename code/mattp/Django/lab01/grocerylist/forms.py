from django import forms
from .models import grocerylister
 
class grocery_form(forms.ModelForm):
    class Meta:
        model = grocerylister
        fields = ['item_label']
 
    item_label = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Item Input'}))
