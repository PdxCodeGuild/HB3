from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class chirp(models.Model):
    text = models.CharField(max_length= 130, default='')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
#     # datetime = models.DateTimeField(default=timezone.now)