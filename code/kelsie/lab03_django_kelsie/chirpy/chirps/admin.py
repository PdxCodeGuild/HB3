from django.contrib import admin
from .models import Chirp, ImgModel

# Register your models here.
admin.site.register(Chirp)
admin.site.register(ImgModel)
