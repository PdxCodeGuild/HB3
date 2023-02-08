from django.shortcuts import render, redirect
from .forms import GroceryForm
from .models import GroceryItem, ItemComplete
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
    context = {"list":list, "form":form}

    if form.is_valid():
        new_item = GroceryItem(itemDescription = request.POST['itemDescription'])
        new_item.save()

        return render (request, "index.html", context)
    

def completed_item(request, item_id):
    finished_item = GroceryItem.objects.get(pk=item_id)
    list = GroceryItem.objects.order_by("id")
    f_list = ItemComplete.objects.order_by("id")
    form = GroceryForm(request.POST)
    context = {"list":list, "form":form, "f_list":f_list}
    if finished_item.is_complete():
        f_item = ItemComplete(itemDescription = request.POST['itemDescription'])
        f_item.save()
        return render (request, "index.html", context)


def deleted_item(request, item_id):
    item = GroceryItem.objects.get(pk=item_id)
    item.delete()
    return (redirect('index'))