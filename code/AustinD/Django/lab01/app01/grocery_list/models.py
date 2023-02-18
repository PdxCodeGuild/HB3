from django.db import models

class GroceryItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text_description} {self.created_date} {self.completed_date} {self.is_completed}'
