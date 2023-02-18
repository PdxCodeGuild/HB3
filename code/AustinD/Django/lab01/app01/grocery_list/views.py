from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import date
from .forms import GroceryForm
from .models import GroceryItem

def grocery_items(request):
    grocery_list_all_items = GroceryItem.objects.all()
    context = {'all_list': grocery_list_all_items, 'form': GroceryForm()}
    return render(request, 'grocery_list/grocery_list.html', context)

def add_grocery_item(request):
    if request.method == "POST":
        form = GroceryForm(request.POST)
        if form.is_valid():
            item_input = form.save(commit=False)
            item_input.created_date = date.today()
            item_input.save()
            return HttpResponseRedirect(reverse('gl:grocery_list'))
    else:
        form = GroceryForm()
    context = {'form': form}
    return render(request, 'grocery_list/grocery_list.html', context)

def remove_grocery_item(request, id):
    item = get_object_or_404(GroceryItem, id=id)
    item.delete()
    return HttpResponseRedirect(reverse('gl:grocery_list'))

def complete_grocery_item(request, id):
    item = get_object_or_404(GroceryItem, id=id)
    item.is_completed = True
    item.completed_date = date.today()
    item.save()
    return HttpResponseRedirect(reverse('gl:grocery_list'))
