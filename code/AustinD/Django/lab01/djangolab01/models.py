from django.db import models

class GroceryItem(models.Model):
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)
    completed_flag = models.BooleanField(default=False)

    class Meta:
        app_label = 'djangolab01'

    
    def __str__(self):
        return self.description
