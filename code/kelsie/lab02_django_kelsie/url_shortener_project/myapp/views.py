from django.shortcuts import render
from django.http import HttpResponse
from .models import ShortURL
from .forms import LongURL
import random, string
# Create your views here.


def index(request):
    form = LongURL()
    return render(request, 'index.html', {"form":form})





def redirect(request):
    form = LongURL(request.POST)
    if form.is_valid():
        item = ShortURL(short_url = request.POST['long_url'])
        short_url = ''.join(random.choice(string.ascii_letters) for x in range(10))
        item.save()
    context = {"item":item, "short_url":short_url}
    return render(request, 'index.html', context)


