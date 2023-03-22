from django.db import models

class GroceryItem(models.Model): 
    # Note to self: models.models is a built in class you need to remember
    # giving the text only up to 200 characters becuase.. thats enough
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    #this covers my boolean statements
    completed_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
# makes sure this returns as a string.. in case there are numbers
    def __str__(self):
        return self.text