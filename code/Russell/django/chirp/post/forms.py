from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    post_text = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={
            "placeholder": "Squeak Your Squawks!",
            "class":"form-control",
            }
            ),
            label="",
        )
    
    class Meta:
        model = Post
        exclude = ('author',)

class RegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']