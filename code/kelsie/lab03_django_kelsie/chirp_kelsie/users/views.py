from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    elif request.method == 'GET':
            form = UserForm()
            return render(request, 'login.html', {"form":form})
 


def signUpView(request):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
    
    return render(request, 'signup.html')
 

def logout_view(request):
    logout(request)