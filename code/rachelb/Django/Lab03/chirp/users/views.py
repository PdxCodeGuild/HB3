from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.

def register(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Account Created.')
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'user/register.html',{'form':form})
