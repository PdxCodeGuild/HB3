from django.db import models
from django.contrib.auth.models import AbstractUser
from pokemon.models import Pokemon
# Create your models here.
class User(AbstractUser):
    pokeball = models.ManyToManyField(Pokemon)

    def __str__(self):
        return self.username