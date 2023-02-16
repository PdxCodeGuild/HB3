from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'URL_shortener_v1/index.html')
    # return HttpResponse('ok')