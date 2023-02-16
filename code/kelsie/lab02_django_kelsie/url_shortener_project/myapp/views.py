from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ShortURL, Click
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

                host_header = request.META.get('HTTP_HOST')
                ip_address = request.META.get('REMOTE_ADDR')
                new_click = Click(host_header=host_header, ip_address=ip_address, short_url=new_info)
                new_click.save()

        return HttpResponseRedirect(new_info.long_url)
 