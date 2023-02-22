from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import urlShortener
from django.http import HttpResponseRedirect
import random
import string

# Create your views here.
def index(request):
    return render(request,'URL_shortener_v1/index.html')
    # return HttpResponse('ok')

# 2 views: one to submit a url and one to redirect the user.  Use djangos HTTPResponseRedirect
# to handle redirecting users

def URLsubmit(request): # a view for recieving the URL submission
    # return HttpResponse('you are at the URLsubmit page')  #DEBUG

    URL_Tag_lead = 'littleURL/'

    if request.method=='POST':   # if the form has been submitted to this url
        # print(request.POST['URLshortenInput'])  #DEBUG
        
        #  Generate a list of 6 random numbers, which can then be used 
        letter_string_random = ""
        # loop 6 times
        for n in range(6):
            # generate a random number
            letter_rand = random.choice(string.ascii_letters)
            letter_string_random += letter_rand
        # end for
        print(letter_string_random)

        URL_user_input = urlShortener(url=request.POST['URLshortenInput'],
                                      code = f'{URL_Tag_lead}{letter_string_random}')

        URL_user_input.save()
        return HttpResponseRedirect(reverse('URL_shortener_v1:Input_myurl'))  

    else:
        # display the links of the database
        submit_url = urlShortener.objects.all()
        context = {'url_link_list': submit_url}
        return render(request,'URL_shortener_v1/urlshortener.html',context)
        
    # return HttpResponse('ok')
    # print(submit_url)  # DEBUG
    # context = {'url_data':submit_url}
    # return render(request,'URL_shortener_v1/urlshortener.html')
    # return HttpResponseRedirect('/mypath')  # Not sure how to use this??
    

def URLredirect(request,id):
    redirect_url = urlShortener.objects.get(id=id)
    print(redirect_url) # DEBUG
    
    # return render(request,'URL_shortener_v1/index.html',context)
    return HttpResponseRedirect(redirect_url.url)  
    # return HttpResponseRedirect(reverse('myapp:myview'))  # Not sure how to use this??