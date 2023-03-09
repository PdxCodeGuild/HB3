from django.contrib import admin
from .models import *

#you also need to migrate after you have register them
#dont forget to register your models after you make them
# Register your models here.
admin.site.register(chirp)