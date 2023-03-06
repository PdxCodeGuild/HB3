from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

chirps=[{'username':'rachel', 'text':'Today this lab is driving me insane'}]

def post(request):
    context = {'chirps': chirps }
    return render(request, 'posting/Feed.html', context)