from django import forms

class GroceryForm(forms.Form):
    input_item = forms.CharField(label='', max_length=100,
    widget = forms.TextInput(attrs={'placeholder': 'Enter Grocery Item'}))


