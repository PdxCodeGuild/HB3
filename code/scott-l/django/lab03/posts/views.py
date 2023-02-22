from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def postsIndex(request):
    context = {'postsIndex':'posts Index placeholer'}
    return render(request, 'posts/postsIndex.html',context)