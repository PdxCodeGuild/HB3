from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
from .models import Profile
from posts.models import Chirp

User = get_user_model()

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
        else :
            form = UserRegistrationForm()
        return render(request, 'users/register.html', {"form":form})

    if request.method == 'GET':
            form = UserRegistrationForm()
            return render(request, 'registration/login.html', {"form":form})
 


@login_required
def profile_view(request, slug):
    p = Profile.objects.filter(slug=slug).first()
    u = p.user
    user_chirps = Chirp.objects.filter(user_name=u)
    context = { 
        'u':u,
        'chirps':user_chirps
        }
    return render(request, 'users/profile.html', context)


