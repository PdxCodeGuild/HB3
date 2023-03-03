from django.db import models

# Create your models here.
class PokemonType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField(max_length=200)
    image_back = models.CharField(max_length=200)
    types = models.ManyToManyField(PokemonType, related_name='types')

    def __str__(self):
        return self.name

class Notes(models.Model):
    note = models.TextField(null=True)