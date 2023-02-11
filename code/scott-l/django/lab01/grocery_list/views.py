from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import GroceryItem
from datetime import date
from .forms import GroceryForm

# Create your views here.
# request handler or actions 

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Scott'}) 

def grocery_items(request):

    grocery_list_all_items = GroceryItem.objects.all()
    print(grocery_list_all_items) # DEBUG
    context = {'all_list':grocery_list_all_items,'form':GroceryForm}
    return render(request,'grocery_list/grocery_list.html', context )

def add_grocery_item(request):
    if request.method == "POST":  # recieving a form submission
        print(request.POST) # DEBUG verify recieved the form data
        # create an instance of the form from the form data
        form = GroceryForm(request.POST)
        if form.is_valid():
            # get the data out of the form
            print(form)
            item_description =  form.cleaned_data['input_item']
            item_created_date = date.today()
            print("Today date is: ", date.today())  #DEBUG
            item_booleanFlag  = False
            # create an instance of the model from the data
            item_input = GroceryItem(text_description=item_description, created_date=item_created_date,completed_date='',booleanFlag=item_booleanFlag )
            # save a new record to the database
            item_input.save()
            
            # if the form is invalid, just sent it back to the template
            return HttpResponseRedirect(reverse('gl:grocery_list'))
    else:  # recieving a GET request
        form = GroceryForm()
    return render(request,'grocery_list/grocery_list.html') # pass the form to the template


# def index(request):
#     imgs = myImage.objects.all()
#     return render(request, 'index.html',{'imgs':data})

# def upload_picture(request):
#     img=request.FILES.get('picture')
#     title = request.POST['title']
#     new_img = myImage(title=title, img=img)
#     new_img.save()
#     return redirect('/')

