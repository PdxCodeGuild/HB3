from django.db import models

class GroceryItem(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
