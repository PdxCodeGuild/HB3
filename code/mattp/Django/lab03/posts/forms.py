from django import forms

from .models import chirp_model
 
class chirp_form(forms.ModelForm):
    class Meta:
        # post_field = forms.CharField(max_length=200)
        model = chirp_model
        fields = ['chirp_text']
        #fields = "__all__"
    # chirp_label = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Item Input'}))
    
