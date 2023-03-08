from django.shortcuts import render

# Create your views here.
post = [{'user_name':'rachel','text':'This time things will be organized'}]

def home(request):
    context= {'posts':post}
    return render(request,'posting/home.html',context)

