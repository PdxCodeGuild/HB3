from django.db import models

# Create your models here.

class ShortURL(models.Model):
    long_url = models.CharField(max_length=500, default=0)
    short_url = models.CharField(max_length=8, blank=True)
    
    def __str__(self):
        return f'{self.short_url} {self.long_url}'
        