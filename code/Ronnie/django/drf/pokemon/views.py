from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Pokemon
# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')
