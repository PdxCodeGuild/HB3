from django.db import models

# Create your models here.
class Chirp(models.Model):
    chirp = models.TextField(max_length=128)