from django.db import models
from django.utils import timezone

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=20)
    date_created = models.DateField(default=timezone.now)
    date_completed = models.CharField(null = True, blank=True, max_length=120)
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
