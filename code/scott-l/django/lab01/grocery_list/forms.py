from django import forms

class GroceryForm(forms.Form):
    input_item = forms.CharField(label='Input Item', max_length=100)
    