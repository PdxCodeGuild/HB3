from django import forms
from .models import make_short

class ShortenerForm(forms.ModelForm):
    
    url_l = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))
    
    class Meta:
        model = make_short

        fields = ('long_url',)