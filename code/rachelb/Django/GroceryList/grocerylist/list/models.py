from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    description = models.CharField(max_length= 30)
    created_date = models.IntegerField()
    completed_date = models.IntegerField()
    complete = models.CharField(max_length=3)
    incomplete = models.CharField(max_length=3)
    
    def __str__(self):
        return self.description