from django.db import models

# Create your models here.

class Items(models.Model):
    content = models.TextField()