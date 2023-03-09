from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import chirp_model
from .forms import chirp_form
from .models import chirp_model
from django.shortcuts import reverse 
from django.contrib.auth.models import User

# Create your views here.

# def add_item(request):
#     if request.method == "POST":
#         form = chirp_form(request.POST)
#         if form.is_valid():
#             post_input = form.save(commit=False)
#             post_input.save()
#             return HttpResponseRedirect(reverse('myproject:chirp_form'))
#     else:
#         form = chirp_form()
#     context = {'form': form}
#     return render(request, 'index.html', context)

def posts(request):
    form = chirp_form(request.POST, request.FILES)
    
    if form.is_valid:
        caption = request.POST.get('chirp_text')
        new_post = chirp_model.objects.create(chirp_text = caption, author=request.user)
        return HttpResponseRedirect(reverse("users:index"))
