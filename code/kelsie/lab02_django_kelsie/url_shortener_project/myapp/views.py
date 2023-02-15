from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ShortURL
from .forms import LongURL
import random, string
# Create your views here.


def index(request):
        form = LongURL()
        return render(request, 'index.html', {"form":form})



def redirect(request):
        if request.method == 'POST':
            form = LongURL(request.POST)
            if form.is_valid():
                long_url = request.POST['long_url']
                short_url = ''.join(random.choice(string.ascii_letters) for x in range(10))
                new_info = ShortURL(short_url=short_url, long_url=long_url)
                new_info.save()
    
        return HttpResponseRedirect(long_url)
 