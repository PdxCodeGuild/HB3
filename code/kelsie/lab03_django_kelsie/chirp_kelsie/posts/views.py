from django.shortcuts import render

# Create your views here.
def index(request):
    chirp = request.POST['chirp']
    return render (request, 'login.html', {"chirp":chirp})