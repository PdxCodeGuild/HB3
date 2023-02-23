from django.db import models
from .utils import create_shortened_url

# Create your models here.
class Shortener(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    long_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True, blank=True)
    times_followed = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def save(self, *args, **kwargs):
       if not self.short_url:
            # pass the model that is saved
            self.short_url = create_shortened_url(self)
            super().save(*args, **kwargs)