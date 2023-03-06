from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str___(self):
        return self.user.username

#Look at ManyToManyField 

# class chirp(models.Model):
#     text = models.CharField(max_length= 130, default='')
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
    # datetime = models.DateTimeField(default=timezone.now)
