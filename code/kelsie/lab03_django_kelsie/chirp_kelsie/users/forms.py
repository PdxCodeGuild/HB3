from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

