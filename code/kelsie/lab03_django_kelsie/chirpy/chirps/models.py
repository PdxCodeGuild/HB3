from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Chirp(models.Model):
    text = models.TextField(max_length=128, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text, self.author, self.date_posted}'

class ImgModel(models.Model):
    my_image = models.ImageField(upload_to='images/')
    caption = models.TextField(max_length=128, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.my_image, self.caption, self.author}'
