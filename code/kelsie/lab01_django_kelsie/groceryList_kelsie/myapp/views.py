from django.shortcuts import render, redirect
from .forms import GroceryForm
from .models import GroceryItem
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    form = GroceryForm()
    list = GroceryItem.objects.all
    context = {"list":list, "form":form}

    return render (request, "index.html", context)


@require_POST
def add_item(request):
    form = GroceryForm(request.POST)
    list = GroceryItem.objects.order_by("id")
    context = {"list":list, "form":form}

    if form.is_valid():
        new_item = GroceryItem(itemDescription = request.POST['itemDescription'])
        new_item.save()

        return render (request, "index.html", context)
    




