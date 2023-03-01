from django.shortcuts import render
from .forms import ChirpForm
from .models import Chirp
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    form = ChirpForm()
    list = Chirp.objects.all().order_by('-date_posted')
    context = {"list":list, "form":form}

    return render(request, "home.html", context)




def addChirp(request):
    form = ChirpForm(request.POST)
    list = Chirp.objects.all().order_by('-date_posted')
    content = request.POST['text']
    author = request.user
    new_chirp = Chirp(text=content, author=author)
    new_chirp.save()

    context = {"list":list, "form":form}

    return render(request, "home.html", context)



def profileView(request):
    form = ChirpForm(request.POST)
    list = Chirp.objects.filter(author=request.user).order_by('-date_posted')

    context = {"list":list, "form":form}

    return render(request, "home.html", context)