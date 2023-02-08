from django.db import models
from django.utils import timezone 
from django.utils.timezone import datetime
from django.urls import reverse

# Create your models here.
class GroceryItem(models.Model):
    itemDescription = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.itemDescription

class ItemComplete(models.Model):
    itemDescription = models.CharField(max_length=500)
    completed = models.BooleanField(default=True)
    
    def __str__(self):
        return self.itemDescription