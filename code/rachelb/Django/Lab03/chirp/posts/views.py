from django.shortcuts import render
from . models import chirps
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    context= {'chirps': chirps.objects.all}
    return render(request,'posting/home.html',context)

# Django has decorator page that allows users to homepage only after signing in 