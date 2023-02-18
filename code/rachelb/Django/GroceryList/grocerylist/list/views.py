from django.shortcuts import render
from .models import GroceryItem

# Create your views here.
# CRUD - create retrieve update delete list

def index(request):
    items = GroceryItem.objects.all()
    context = {'items':items}
    return render(request, 'index.html', context)

def index_retrieve(request, id):
    item = GroceryItem.objects.get(pk=id)
    context = {"name": item}
    return render(request, "items.html", context)