from django.shortcuts import render, redirect
from .models import myImage
# Create your views here.
def index_404(request):
    imgs = myImage.objects.all()
    context = {
        'imgs': imgs,
    }
    return render(request, 'index.html', context)

def upload_picture(request):
    img = request.FILES.get('picture')
    title = request.POST['title']
    new_img = myImage(title=title, img=img)
    new_img.save()
    return redirect('/')