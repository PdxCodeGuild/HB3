from django.shortcuts import render
from django.http import HttpResponse
from .models import GroceryItem

# Create your views here.
# request handler or actions 

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Scott'}) 

def grocery_items(request):

    item_info = {'text_description': 'Blank',
    'created_date':'date',
    'completed_date':'date',
    'boolean_response': 'true/false' }

    return render(request,'grocery_list/grocery_list.html', item_info )


