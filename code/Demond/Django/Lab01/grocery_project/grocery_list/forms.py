from django import forms
from .models import GroceryItem

# This is used to actually create a new input for my list
class GroceryItemForm(forms.ModelForm):
    class Meta:
        # note to self: model is basically clarifying it to be the grocery item class.
        model = GroceryItem
        fields = ['text']
        labels = {'text': ''}