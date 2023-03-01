from django.shortcuts import render, get_object_or_404
from .models import URL
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if request.method =='POST':
        link = URL()
        link.long_url = request.POST['long_url']
        link.generate_code()
        link.save()
        return render(request, 'index.html', {"link":link})
    return render(request, 'index.html')

def onedirection(request, code):
    link = get_object_or_404(URL, code=code)
    return HttpResponseRedirect(link.long_url)