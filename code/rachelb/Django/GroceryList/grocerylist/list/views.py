from django.shortcuts import render, redirect
from .models import GroceryItem

from .forms import GroceryItemForm

# Create your views here.
# CRUD - create retrieve update delete list

def index(request):
    items = GroceryItem.objects.all()
    context = {'items':items}
    return render(request, 'index.html', context)


def index_retrieve(request):
    item = GroceryItem.objects.get()
    context = {'name':item}
    return render(request, 'items.html', context)
# def index_retrieve(request, id):
#     item = GroceryItem.objects.get(pk=id)
#     context = {"name": item}
#     return render(request, "items.html", context)

def index_create(request):
    form = GroceryItemForm()

    if request.method == 'POST':
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {"form": form }
    return render(request, "grocerylist_create.html",context)
