from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
def user_registration(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    print(username)
    print(password)
    print(email)
    return HttpResponse('User created!')
    # user = User.objects.create_user(username, email, password)
    # return redirect('/')

from django.contrib.auth import authenticate, login, logout
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/u/profile', {'user':request.user})
    else: 
        return HttpResponse('Login credential did not match')

from django.contrib.auth.decorators import login_required
def reset_password(request):
    username = request.POST['username']
    new_password = request.POST['new_password']
    user = User.objects.get(username=username)
    user.set_password(new_password)
    user.save()
    return redirect('/')

def signout_view(request):
    logout(request)
    return redirect('/')

# @login_required
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return HttpResponse('you must be logged in to see this view')