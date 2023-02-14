from django.contrib import admin

# Register your models here.

from .models import GroceryItem, DateUpdated, MyImages

admin.site.register(GroceryItem)
admin.site.register(DateUpdated)
admin.site.register(MyImages)