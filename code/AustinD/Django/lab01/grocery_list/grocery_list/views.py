from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import GroceryItem

def grocery_list(request):
    if request.method == 'POST':
        description = request.POST['description']
        item = GroceryItem(description=description)
        item.save()
        return redirect('grocery_list')

    incomplete_items = GroceryItem.objects.filter(completed=False)
    complete_items = GroceryItem.objects.filter(completed=True)
    context = {
        'incomplete_items': incomplete_items,
        'complete_items': complete_items,
    }
    return render(request, 'grocery_list.html', context)

def mark_complete(request, item_id):
    item = GroceryItem.objects.get(pk=item_id)
    item.completed = True
    item.completed_date = datetime.now()
    item.save()
    return redirect('grocery_list')

def mark_incomplete(request, item_id):
    item = GroceryItem.objects.get(pk=item_id)
    item.completed = False
    item.completed_date = None
    item.save()
    return redirect('grocery_list')

def delete_item(request, item_id):
    item = GroceryItem.objects.get(pk=item_id)
    item.delete()
    return redirect('grocery_list')
