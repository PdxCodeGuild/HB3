from django.shortcuts import render
from .models import GroceryItem
from .forms import GroceryItemForm
from django.shortcuts import render, redirect

def index(request):
    incomplete_items = GroceryItem.objects.filter(completed=False)
    complete_items = GroceryItem.objects.filter(completed=True)
    # the above will appropriate the variables/input with the booleans as well as collect the actual data depeding on the type of request below..
    form = GroceryItemForm()

    if request.method == 'POST':
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'incomplete_items': incomplete_items,
               'complete_items': complete_items,
               'form': form}
    return render(request, 'grocery_list/index.html', context)

#this function will find the correct item and actually manipulate it, stores it back and then user request goes back the the index.html
def complete_item(request, item_id):
    item = GroceryItem.objects.get(id=item_id)
    item.completed = not item.completed
    item.save()
    return redirect('index')

#this does same as above with delete
def delete_item(request, item_id):
    item = GroceryItem.objects.get(id=item_id)
    item.delete()
    return redirect('index')