from django.db import models

# Create your models here.

class ShortURL(models.Model):
    long_url = models.URLField
    short_url = models.CharField(max_length=8, blank=True)
    
    def __str__(self):
        return self.short_url
        