from django.shortcuts import render
from django.http import HttpResponse
from .models import grocerylister
# Create your views here.
def index(request):
    list = grocerylister.objects.filter(completed=False)
    
    return render(request, "index.html", {"list": list})

