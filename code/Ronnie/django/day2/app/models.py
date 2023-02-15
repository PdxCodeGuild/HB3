from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    email_address = models.EmailField(max_length=300)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="contacts", to_field="name", default="Portland")

    def __str__(self):
        return self.email_address

class Friends(models.Model):
    title = models.CharField(max_length=250)
    users = models.ManyToManyField(Contact, related_name='friends', blank=True, null=True)

    def __str__(self):
        return self.title

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True, blank=True)
