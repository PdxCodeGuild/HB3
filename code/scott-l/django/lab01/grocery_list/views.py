from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import GroceryItem

# Create your views here.
# request handler or actions 

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Scott'}) 

def grocery_items(request):

    grocery_list_all_items = GroceryItem.objects.all()
    print(grocery_list_all_items) # DEBUG
    context = {'all_list':grocery_list_all_items}
    return render(request,'grocery_list/grocery_list.html', context )

def add_grocery_item(request):
    if request.method == "POST":
        print(request.POST) # DEBUG verify recieved the form data

        return HttpResponseRedirect(reverse('gl:grocery_list'))
        
    
    else:
        return render(request,'grocery_list/grocery_list.html')


# def index(request):
#     imgs = myImage.objects.all()
#     return render(request, 'index.html',{'imgs':data})

# def upload_picture(request):
#     img=request.FILES.get('picture')
#     title = request.POST['title']
#     new_img = myImage(title=title, img=img)
#     new_img.save()
#     return redirect('/')

