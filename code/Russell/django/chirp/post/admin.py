from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Post, Profile


admin.site.register(Post)

admin.site.unregister(Group)

# # Register Profile
# admin.site.register(Profile)

# Combine User and Profile data
class ProfileUserCombo(admin.StackedInline):
    model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Only show username in admin
    fields = ['username']
    inlines = [ProfileUserCombo]

# Unregister og User
admin.site.unregister(User)

# Re-register User
admin.site.register(User, UserAdmin)
