from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group, User
from .models import Profile
# Register your models here.

admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
    model = Profile 
    
class UserAdmin(admin.ModelAdmin):
    model = User 
    fields = ["username"]
    inlines = [ProfileInline]
# how to display only certain fields on admin page

# This is unregistering user on admin site
admin.site.unregister(User)

# Reautherizing is with only User field in admin
admin.site.register(User, UserAdmin)

# This is how you register user 
# admin.site.register(Profile)

# Combine user and profile sections
