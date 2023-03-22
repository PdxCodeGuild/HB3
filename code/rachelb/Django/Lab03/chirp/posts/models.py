from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class chirps(models.Model):
    text = models.CharField(max_length= 150, default='')
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    
