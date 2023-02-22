from django import forms

class PostForm(forms.Form):
    chirp = forms.CharField(max_length=128)