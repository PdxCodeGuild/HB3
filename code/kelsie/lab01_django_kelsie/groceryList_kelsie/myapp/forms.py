from django import forms

class GroceryForm(forms.Form):
    itemDescription = forms.CharField(max_length=500)


    