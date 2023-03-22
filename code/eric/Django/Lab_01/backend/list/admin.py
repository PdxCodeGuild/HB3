from django.contrib import admin
from .models import List


class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'completed')

# Register your models here.


admin.site.register(List, ListAdmin)
