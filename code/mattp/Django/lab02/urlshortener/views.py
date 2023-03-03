from django.shortcuts import render, get_object_or_404
from .models import Shortener
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    if request.method == "POST":
        link = Shortener()
        link.url_long = request.POST["url_long"]
        link.generate_code()
        link.save()
        return render(request, "index.html", {"link":link})
    return render(request, "index.html")

def redirectio(request, random_code):
    link = get_object_or_404(Shortener, random_code=random_code)
    return HttpResponseRedirect(link.url_long)