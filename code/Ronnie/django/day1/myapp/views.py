from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("you are at the index")

def about(request):
    return HttpResponse("you are at our about page")