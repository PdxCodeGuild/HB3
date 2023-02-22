from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def usersIndex(request):
    context = {'usersIndex':'users Index placeholer'}
    return render(request, 'users/usersIndex.html',context)