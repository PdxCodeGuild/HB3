from django.db import models
from django.utils import timezone 
from django.utils.timezone import datetime
from django.urls import reverse

# Create your models here.
class GroceryItem(models.Model):
    itemDescription = models.CharField(max_length=500)
    createdDate = models.DateField()
    completedDate = models.DateField()
    completed = models.BooleanField()