from django.shortcuts import render
from .forms import ChirpForm
from .models import Chirp, ImgModel
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    form = ChirpForm()
    list = ImgModel.objects.all().order_by('-date_posted')
    context = {"list":list, "form":form}

    return render(request, "home.html", context)




def addChirp(request):
    form = ChirpForm(request.POST, request.FILES)
    list = ImgModel.objects.all().order_by('-date_posted')
    if form.is_valid:
        caption = request.POST.get('text')
        my_image = request.FILES['my_image']
        author = request.user
        
        new_image = ImgModel(caption=caption, author=author, my_image=my_image)
        new_image.save()
        
        context = {"list":list, "form":form}

        return render(request, "home.html", context)



def profileView(request):
    form = ChirpForm(request.POST)
    list = ImgModel.objects.filter(author=request.user).order_by('-date_posted')

    context = {"list":list, "form":form}

    return render(request, "home.html", context)