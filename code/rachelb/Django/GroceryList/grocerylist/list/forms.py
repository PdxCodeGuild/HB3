from django.forms import ModelForm
from .models import GroceryItem


class GroceryItemForm(ModelForm):
    class Meta:
        model = GroceryItem
        fields = '__all__'

    
