from django import forms

class ChirpForm(forms.Form):
    text = forms.CharField(max_length=128)
