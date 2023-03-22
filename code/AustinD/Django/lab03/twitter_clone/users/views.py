from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseRedirect
from posts.models import BlogPost



# Create your views here.
def usersIndex(request):
    context = {'usersIndex':'users Index placeholder'}
    return render(request, 'usersIndex.html',context)

def user_registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username,
                                        email,
                                        password,
                                        first_name=first_name,
                                        last_name=last_name)
        user.save()
        return render(request, 'login.html')
    else:
        return render(request, 'registration.html') 

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username) #DEBUG
        print(password) #DEBUG
        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            userModelObject = User.objects.get(username=request.user)
            print(userModelObject) #DEBUG
            context = {'userInfo': userModelObject}
            return render(request, 'profileIndex.html',context)
        else:
            return HttpResponse('Login credential did not match')
        
    return render(request, 'users/login.html')  

def user_reset_password(request):
    username = request.POST['username']
    new_password = request.POST['new_password']
    print(username) #DEBUG
    print(new_password) #DEBUG
    user = User.objects.get(username=username)
    user.set_password(new_password)
    user.save()
    return HttpResponse('user reset password')

def user_profile(request):
    if request.user.is_authenticated:
        userModelObject = User.objects.get(username=request.user)
        blogPost0bject = BlogPost.objects.filter(userNamePost=request.user)
        print(userModelObject) #DEBUG
        print(blogPost0bject)  #DEBUG
        context = {'userInfo': userModelObject,
                   'blogPostInfo':blogPost0bject}
        return render(request, 'profileIndex.html',context)

    else: 
        return HttpResponse('you must be logged in to see this view')
    
def user_public_profile(request):
    if request.user.is_authenticated:
        userModelObject = User.objects.get(username=request.user)
        blogPost0bjects = BlogPost.objects.all()
        print(userModelObject) #DEBUG
        context = {'userInfo': userModelObject,
                   'blogPostObjects': blogPost0bjects}
        return render(request, 'postsIndex.html',context)
    else: 
        return HttpResponse('you must be logged in to see this view')


def user_signout(request):
    logout(request)
    return render(request, 'login.html')