from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import URL, Click
from ipware import get_client_ip
# Create your views here.
def index(request):
    if request.method == 'POST':
        link = URL()
        link.long_url = request.POST['long_url']
        link.generate_code()
        link.save()
        return render(request, 'index.html', {'link': link})
    return render(request, 'index.html')

def redirection(request, code):
    link = get_object_or_404(URL, code=code)

    meta_data = Click()
    meta_data.http_referer = request.META['HTTP_REFERER']
    meta_data.ip_address = get_client_ip(request)
    meta_data.url = link
    meta_data.save()
    return HttpResponseRedirect(link.long_url)
