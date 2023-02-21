from django.shortcuts import render, redirect
from .models import Url

def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        u = Url(url=url)
        u.save()
        return render(request, 'urlshorter/index.html', {'short_url': f"{request.scheme}://{request.get_host()}/{u.code}"})
    return render(request, 'urlshorter/index.html')

def redirect_url(request, code):
    try:
        url = Url.objects.get(code=code)
        return redirect(url.url)
    except Url.DoesNotExist:
        return render(request, 'urlshorter/404.html')
