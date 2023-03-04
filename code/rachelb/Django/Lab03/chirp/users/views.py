from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def user(request):
    return render(request, 'Homepage.html',)

def user_login(request):
    return render(request, 'Login.html',)


