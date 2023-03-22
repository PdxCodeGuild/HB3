from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Items

# Create your views here.

def groceries_view(request):
    return render(request, 'groceries.html', {'items': Items.objects.all()})

def add_item_view(request):
    Items(content = request.POST['content']).save()
    return HttpResponseRedirect('/groceries/')

def delete_item_view(request, item_id):
    Items.objects.get(pk=item_id).delete()
    return HttpResponseRedirect('/groceries/')