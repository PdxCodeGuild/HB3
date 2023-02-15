from django.db import models

# Create your models here.
class myImage(models.Model):
    title = models.CharField(max_length=300)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title