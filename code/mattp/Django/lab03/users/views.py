from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from posts.models import chirp_model
from posts.forms import chirp_form
#from .forms import Signupform, Loginform

# Create your views here.

def signup(request):
    if request.method == "POST":
        create_user = User.objects.create_user(
           username = request.POST["username_input"],
           password = request.POST["password_input"], 
        )
    return render(request, "register.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            return HttpResponseRedirect(reverse("users:index"))
        else:
        # Return an 'invalid login' error message.
            print("maybe try again")
    return render(request, "registration/login.html")

def index(request):
    list = chirp_model.objects.all()
    form_store = chirp_form()
    context = {"list":list, "form_store":form_store}
    return render(request, "index.html", context)

