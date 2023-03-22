from django.shortcuts import render, get_object_or_404 # We will use it later

from django.http import HttpResponseRedirect

from .models import Shortify

# Create your views here.

def home_view(request):
    if request.method == 'POST':
        link = Shortify()
        link.long_one = request.POST['input']
        link.generate_code()
        link.save()
        return render(request, 'shortify.html', {'link':link})
    return render(request, 'shortify.html')


def redirection(request, short_one):
    link = get_object_or_404(Shortify, short_one = short_one)
    return HttpResponseRedirect(link.long_one)