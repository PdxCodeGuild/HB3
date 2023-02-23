from django.db import models

# Create your models here.

class GroceryItems(models.Model):
    description = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.description
