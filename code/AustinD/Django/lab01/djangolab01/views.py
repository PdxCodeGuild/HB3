from django.shortcuts import render, redirect
from .models import GroceryItem
from .forms import GroceryItemForm

def grocery_list(request):
    if request.method == 'POST':
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grocery_list')
    else:
        form = GroceryItemForm()
        
    incomplete_items = GroceryItem.objects.filter(completed_flag=False)
    complete_items = GroceryItem.objects.filter(completed_flag=True)
    
    context = {
        'form': form,
        'incomplete_items': incomplete_items,
        'complete_items': complete_items
    }
    return render(request, 'grocery_list.html', context)

def complete_item(request, pk):
    item = GroceryItem.objects.get(pk=pk)
    item.is_completed = True
    item.completed_date = timezone.now()
    item.save()
    return redirect('grocery_list')

def delete_item(request, pk):
    item = GroceryItem.objects.get(pk=pk)
    item.delete()
    return redirect('grocery_list')
