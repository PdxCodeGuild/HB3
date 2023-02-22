from django.contrib import admin
from .models import ShortURL, Click

# Register your models here.

admin.site.register(ShortURL)
admin.site.register(Click)