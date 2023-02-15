from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse
from datetime import datetime

class GroceryItem:
    def __init__(self, description, created_date, completed_date=None, completed=False):
        self.description = description
        self.created_date = created_date
        self.completed_date = completed_date
        self.completed = completed

grocery_items = []

def grocery_list(request):
    if request.method == 'POST':
        description = request.POST['description']
        item = GroceryItem(description=description, created_date=datetime.now())
        grocery_items.append(item)
        return redirect('grocery_list')

    incomplete_items = [item for item in grocery_items if not item.completed]
    complete_items = [item for item in grocery_items if item.completed]
    context = {
        'incomplete_items': incomplete_items,
        'complete_items': complete_items,
    }
    return render(request, 'grocery_list.html', context)

def mark_complete(request, item_id):
    item = grocery_items[item_id]
    item.completed = True
    item.completed_date = datetime.now()
    return redirect('grocery_list')

def mark_incomplete(request, item_id):
    item = grocery_items[item_id]
    item.completed = False
    item.completed_date = None
    return redirect('grocery_list')

def delete_item(request, item_id):
    grocery_items.pop(item_id)
    return redirect('grocery_list')

urlpatterns = [
    path('', grocery_list, name='grocery_list'),
    path('mark_complete/<int:item_id>/', mark_complete, name='mark_complete'),
    path('mark_incomplete/<int:item_id>/', mark_incomplete, name='mark_incomplete'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
]
