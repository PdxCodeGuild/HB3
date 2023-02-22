from django.db import models
from django import forms

# Create your models here.

# 1 model to store the long url and short code

class urlShortener(models.Model):
    code = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    

    def __str__(self):
        return f'{self.code},{self.url}'


    
