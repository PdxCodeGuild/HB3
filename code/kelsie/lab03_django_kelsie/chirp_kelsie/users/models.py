from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.
class UserLogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='user')

    def __str__(self):
        return str(self.user.username)
        