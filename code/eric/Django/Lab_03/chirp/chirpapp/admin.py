from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Chirp

# unregister Groups
admin.site.unregister(Group)

# add profile info into the user info
class ProfileInline(admin.StackedInline):
    model = Profile

# extend the user model
class UserAdmin(admin.ModelAdmin):
    model = User
    # display username fields on the admin page
    fields = ["username"]
    inlines = [ProfileInline]

# unregister the user
admin.site.unregister(User)

# reregister the user and profile
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)

admin.site.register(Chirp)
