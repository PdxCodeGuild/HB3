from django import forms

class GroceryForm(forms.Form):
    item = forms.CharField(max_length=500, required=False)
