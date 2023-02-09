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
 

def deleted_item(request,item_id):
    item = GroceryItem.objects.get(pk=item_id)
    item.delete()
    return redirect('index')


def completed_item(request, item_id):
    form = GroceryForm(request.POST)
    list = GroceryItem.objects.order_by("id")
    finished_item = GroceryItem.objects.get(pk=item_id)
    finished_item.complete = True

    context = {"finished_item":finished_item, "list":list, "form":form}
    return render (request, "index.html", context)


