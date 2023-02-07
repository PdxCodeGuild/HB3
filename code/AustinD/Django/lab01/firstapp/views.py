from django.shortcuts import render, redirect
from .forms import GroceryItemForm
from .models import GroceryItem

def grocery_list(request):
    if request.method == 'POST':
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grocery_list')
    else:
        form = GroceryItemForm()
    incomplete_items = GroceryItem.objects.filter(completed=False)
    complete_items = GroceryItem.objects.filter(completed=True)
    return render(request, 'grocery_list/grocery_list.html', {'form': form, 'incomplete_items': incomplete_items, 'complete_items': complete_items})

def mark_complete(request, pk):
    item = GroceryItem.objects.get(pk=pk)
    item.completed = True
    item.completed_date = timezone.now()
    item.save()
    return redirect('grocery_list')

def mark_incomplete(request, pk):
    item = GroceryItem.objects.get(pk=pk)
    item.completed = False
    item.completed_date = None
    item.save()
    return redirect('grocery_list')

def delete_item(request, pk):
    item = GroceryItem.objects.get(pk=pk)
    item.delete()
    return redirect('grocery_list')
