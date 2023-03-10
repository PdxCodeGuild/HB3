from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    post_text = models.CharField(max_length=138)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    
    def __str__(self):
        return self.post_text + ' ' + self.author.username