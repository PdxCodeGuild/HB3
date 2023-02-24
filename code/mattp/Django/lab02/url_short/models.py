from django.db import models
from .utils import create_short

# Create your models here.

class make_short(models.Model):

    url_long = models.URLField()

    url_short = models.CharField(max_length=20, unique=True, blank=True)

    class Meta:
        ordering = ""
        
    def __str__(self):
        return f'{self.url_long} to {self.url_short}'
    
    def save(self, *args, **kwargs):
        if not self.url_short:
            self.url_short = create_short(self)
            
        super().save(*args, **kwargs)
        
    
    
