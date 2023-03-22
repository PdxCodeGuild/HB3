from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *
# Create your views here.
@login_required
def post_tweet(request):
    if request.method == 'POST':
        newChirp = chirp.objects.create(user=request.user, text=request.POST["Chirp"])
        #objects.create() django built in
        # if len(chirping) > 128:
        #     messages.error(request, 'Tweet cannot exceed 128 characs')
            #this is from the build in messages
        return redirect('home')
        # else:
    return render(request, 'tweet.html')