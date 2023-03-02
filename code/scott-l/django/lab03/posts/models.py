from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Notes 
# user - Foriegn Key
# Text box
# date field (option)

class BlogPost(models.Model):
    text = models.CharField(max_length=120)
    likes = models.IntegerField(default=0)
    userNamePost = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return f'{self.text} {self.likes} {self.userNamePost}'
