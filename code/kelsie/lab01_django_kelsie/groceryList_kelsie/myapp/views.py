from django.shortcuts import render, redirect
from .forms import GroceryForm
from .models import GroceryItem, DateUpdated
from django.views.decorators.http import require_POST
# Create your views here.


def index(request):
    form = GroceryForm()
    list = GroceryItem.objects.order_by("id")
    context = {"list":list, "form":form}

    return render (request, "index.html", context)


@require_POST
def add_item(request):
    form = GroceryForm(request.POST)
    list = GroceryItem.objects.order_by("id")
    date = DateUpdated()
    context = {"list":list, "form":form, "date":date}

    if form.is_valid():
        new_item = GroceryItem(itemDescription = request.POST['item'])
        new_item.save()

    return render (request, "index.html", context)


def completed_item(request, item_id):
    form = GroceryForm(request.POST)
    date = DateUpdated()
    list = GroceryItem.objects.order_by("id")
    item = GroceryItem.objects.get(pk=item_id)
    item.completed=True
    item.save()
    context = {"list":list, "form":form, "date":date}

    return render (request, "index.html", context)


def deleted_item(request, item_id):
    form = GroceryForm(request.POST)
    list = GroceryItem.objects.order_by("id")
    date = DateUpdated()
    item = GroceryItem.objects.get(pk=item_id)
    item.delete()
    context = {"list":list, "form":form,"date":date}
    
    return render (request, 'index.html', context)