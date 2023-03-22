from django.db import models
from django.contrib.auth.models import User
#Django default user model

# Create your models here.

class chirp(models.Model): #models.Model, required
    user = models.ForeignKey(User, default = None, on_delete=models.CASCADE)
    text = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.user} - {self.text}"
    #this is essential as we need to convert this into string for our views. 