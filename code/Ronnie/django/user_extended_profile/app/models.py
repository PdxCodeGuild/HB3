from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=10, blank=True, null=True)

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user_profile')
#     phone_number = models.CharField(max_length=20)