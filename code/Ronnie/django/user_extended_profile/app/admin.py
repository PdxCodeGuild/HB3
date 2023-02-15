from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
UserAdmin.fieldsets += ('Contact Info', {'fields': ['phone_number']}),
admin.site.register(User, UserAdmin)