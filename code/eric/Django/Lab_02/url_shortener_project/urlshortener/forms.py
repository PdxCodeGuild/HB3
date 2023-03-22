# urlshortener/forms.py

from django import forms
from .models import Shortener

class shortener_form(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))
    class Meta:
        model = Shortener
        fields = ('long_url',)
