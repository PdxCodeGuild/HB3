from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def usersIndex(request):
    context = {'usersIndex':'users Index placeholder'}
    return render(request, 'users/usersIndex.html',context)

def user_registration(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    print(username)
    print(password)
    print(email)
    return HttpResponse('user registration')

def user_reset_password(request):
    return HttpResponse('user reset password')

def user_profile(request):
    return HttpResponse('user profile')

def user_login(request):
    return HttpResponse('user login')

def user_signout(request):
    return HttpResponse('user signout')