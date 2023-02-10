from django.db import models
from django.utils import timezone 
from django.utils.timezone import datetime
from django.urls import reverse

# Create your models here.
class GroceryItem(models.Model):
    itemDescription = models.CharField(max_length=500, null=True, blank=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.itemDescription

class DateUpdated(models.Model):
    date_time = datetime.now()
    date = date_time.strftime("%x")

    def __str__(self):
        return self.date

class ItemComplete(models.Model):
    itemDescription = models.CharField(max_length=500, null=True, blank=True)
    completed = models.BooleanField(default=True)
    
    def __str__(self):
        return self.itemDescription


class MyImages(models.Model):
    my_image = models.ImageField(upload_to='images/')