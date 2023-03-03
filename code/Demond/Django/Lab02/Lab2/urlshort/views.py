from django.shortcuts import render, get_object_or_404
from .models import shortener
from django.http import HttpResponseRedirect
# Create your views here.
def url_shortner(request): 
    if request.method == "POST":
        shortened = shortener()
        shortened.url = request.POST["Url"]
        shortened.generate_code()
        shortened.save()
        return render(request, "index.html", {"shortened": shortened})
    return render(request, "index.html")

def user_redirect(request, code):
    link = get_object_or_404(shortener, code=code)
    return HttpResponseRedirect(link.url)