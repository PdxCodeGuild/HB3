from django import forms

class GroceryForm(forms.Form):
    itemDescription = forms.CharField(max_length=500)
    createdDate = forms.DateField()
    completedDate = forms.DateField()
    
    