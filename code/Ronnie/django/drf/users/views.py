from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages

def user_registration(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']
		print(username)
		print(password)
		print(email)
		user = User.objects.create_user(username, email, password)
		return redirect('/')
	return render(request, 'registration/register.html')

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})