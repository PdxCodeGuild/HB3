from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import grocerylister
from datetime import date
from django.urls import reverse
# Create your views here.
def index(request):
    list = grocerylister.objects.all()
    
    return render(request, "index.html", {"list": list})

def item_add(request):
    user_input = request.POST['add_item']
    item = grocerylister(name=user_input, completed=False)
    item.save()
    return redirect("/")

def delete_item(request, id):
    remove_item = grocerylister.objects.get(pk=id)
    remove_item.delete()
    return redirect("/")

def complete_item(request, id):
    item = get_object_or_404(grocerylister, id=id)
    item.completed = True
    item.completed_date = date.today()
    item.save()
    return redirect("/")

