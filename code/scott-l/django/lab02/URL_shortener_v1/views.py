from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import urlShortener
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'URL_shortener_v1/index.html')
    # return HttpResponse('ok')

# 2 views: one to submit a url and one to redirect the user.  Use djangos HTTPResponseRedirect
# to handle redirecting users

def URLsubmit(request):
    submit_url = urlShortener.objects.all()
    print(submit_url)  # DEBUG
    context = {'url_data':submit_url}
    return render(request,'URL_shortener_v1/index.html',context)
    # return HttpResponseRedirect('/mypath')  # Not sure how to use this??
    # return HttpResponseRedirect(reverse('myapp:myview'))  # Not sure how to use this?? Not applicable

def URLredirect(request):
    redirect_url = urlShortener.objects.all()
    print(redirect_url) # DEBUG
    context = {'url_data':redirect_url}
    return render(request,'URL_shortener_v1/index.html',context)
    # return HttpResponseRedirect('/mypath')  # Not sure how to use this??
    # return HttpResponseRedirect(reverse('myapp:myview'))  # Not sure how to use this??