from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.
def list(request):
    items = GroceryItems.objects.all()

    form = GroceryItemsForm()

    if request.method =='POST':
        form = GroceryItemsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'items': items,'form':form}
    return render(request, 'items/Items.html', context)

def Edit(request, pk):
    item = GroceryItems.objects.get(id=pk)
    
    form = GroceryItemsForm(instance=item)

    if request.method == 'POST':
        form = GroceryItemsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'items/Edit.html',context)

def Delete(request,pk):
    item = GroceryItems.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
        

    context = {'item':item}
    return render(request, 'items/Delete.html',context)


   

# def Delete(request, pk):
#     items = GroceryItems.objects.get(id=pk)
#     items.delete()
#     return redirect('/')
# Make sure to redirect the function to a certain page