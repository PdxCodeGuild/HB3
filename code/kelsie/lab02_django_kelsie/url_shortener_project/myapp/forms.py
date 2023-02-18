from django import forms
from .models import ShortURL

class LongURL(forms.Form):
    long_url = forms.URLField(label="Enter long URL here")
