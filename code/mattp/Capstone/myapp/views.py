from django.shortcuts import render
from .forms import ZipcodeForm, ContactForm
from .models import FishSpeciesModel

# # Create your views here.
def home(request):
    if request.method == "POST":
        zip_code = request.POST["zip_code"]
        fishlist = FishSpeciesModel.objects.filter(fish_zip__zip_code = zip_code)
        print(fishlist)
        return render(request, "home.html", {'fishlist': fishlist})
    
    form = ZipcodeForm()
    context = {"form": form}
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')

def fish_details(request, fish_id):
    fish = FishSpeciesModel.objects.get(pk=fish_id)
    return render(request, 'details.html', {'fish': fish})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to success page or show success message
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)   

def FishView(request):
    return render(request)
    
    
# def about(request):
#     return HttpResponse('you are at the index again')

# def populate_model(request):
#     with open('data.json') as f:
#         data = json.load(f)

#     for obj in data:
#         zipmodel = ZipcodeModel(name=obj['name'], description=obj['description'])
#         zipmodel.save()

#     return render(request, 'success.html')
#