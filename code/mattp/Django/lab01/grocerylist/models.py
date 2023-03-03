from django.db import models
from datetime import date

# Create your models here.
class grocerylister(models.Model):
    name = models.CharField(max_length=250)
    created_date = models.DateField(default=date.today)
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name