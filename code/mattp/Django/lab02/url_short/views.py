from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import make_short
from .forms import ShortenerForm

# Create your views here.

def home_view(request):
    template = 'url_short/home.html'