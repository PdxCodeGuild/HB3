from django import forms

class GroceryForm(forms.Form):
    input_item = forms.CharField(max_length=100)
    