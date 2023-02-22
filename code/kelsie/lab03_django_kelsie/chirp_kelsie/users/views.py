from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    if request.method == 'GET':
            form = UserForm()
            return render(request, 'login.html', {"form":form})
 

def logout_view(request):
    logout(request)