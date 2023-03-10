from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.views.generic import View
from post.models import *


# Create your views here.
def home(request):
    list = chirp.objects.all()
    print(list)
    context = {"list": list}
    return render(request, 'home.html', context)

def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, 'registration/login.html', context)

def my_logout(request):
    auth_logout(request)
    return redirect('step1:home')

class SignupView(View):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('step1:home')

    def get(self, request):
        form = self.form_class()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(self.success_url)
        else:
            return render(request, self.template_name,)
        
class HomeView(TemplateView):
    template_name = 'home.html'