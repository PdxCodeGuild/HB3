from django.db import models

# Create your models here.

class ShortURL(models.Model):
    long_url = models.CharField(max_length=500, default=0)
    short_url = models.CharField(max_length=8, blank=True)
    
    def __str__(self):
        return f'{self.short_url} {self.long_url}'
        


class Click(models.Model):
    host_header = models.CharField(max_length=30, blank=True)
    ip_address = models.CharField(max_length=30, blank=True)
    short_url = models.ForeignKey(ShortURL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ip_address} {self.host_header}'