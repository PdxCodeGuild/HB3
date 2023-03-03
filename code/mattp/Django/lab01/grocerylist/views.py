
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import grocerylister
from .forms import grocery_form
from django.shortcuts import reverse 

# Create your views here.
def index(request):
    list = grocerylister.objects.all()
    
    return render(request, "index.html", {"list": list})


def grocery_items(request):
    list_items = grocery_form.objects.all()
    context = {'all_list': list_items, 'form': grocery_form()}
    return render(request, 'index.html', context)
 
def add_item(request):
    if request.method == "POST":
        form = grocery_form(request.POST)
        if form.is_valid():
            item_input = form.save(commit=False)
            item_input.save()
            return HttpResponseRedirect(reverse('grocery_list:grocery_list'))
    else:
        form = grocery_form()
    context = {'form': form}
    return render(request, 'index.html', context)
 
def remove_item(request, id):
    item = get_object_or_404(grocerylister, id=id)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list:grocery_list'))
 
def completed_item(request, id):
    item = get_object_or_404(grocerylister, id=id)
    item.is_completed = True
    item.save()
    return HttpResponseRedirect('grocery_list:grocery_list')



