from django.forms import ModelForm
from django import forms
from .models import Todo

class RegisterTodo(forms.Form):
    title = forms.CharField(label='title', max_length=250)

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'