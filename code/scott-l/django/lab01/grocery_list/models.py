from django.db import models

# Create your models here.


# Model GroceryItem
class GroceryItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.CharField(max_length=200)
    completed_date = models.CharField(max_length=200)
    boolean  = models.BooleanField()
    def __str__(self):
        return f'{self.text_description}{self.created_date}{self.completed_date}{self.boolean}'

