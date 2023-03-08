from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class chirp_model(models.Model):
    chirp_text = models.TextField(max_length=250, blank=True, null = True)
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.chirp_text}, {self.date}, {self.author}' 