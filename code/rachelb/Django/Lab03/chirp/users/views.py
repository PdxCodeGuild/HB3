from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from django.contrib.auth.form import UserCreationForm
from django.contrib.auth.forms import UserCreationForm

def user_home(request):
    return render(request, 'Homepage.html',)

def user_login(request):
    return render(request, 'Login.html')

def register(request):
    return render(request, 'authenticate/register.html')


