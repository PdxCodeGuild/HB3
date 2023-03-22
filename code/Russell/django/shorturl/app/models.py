from django.db import models
from .utils import create_short_url
from string import ascii_letters, digits
import random


POSSIBLE_CHARS = ascii_letters + digits


class Shortify(models.Model):

    long_one = models.URLField()

    short_one = models.CharField(max_length=7, unique=True, blank=True)


    def generate_code(self):

        self.short_one = "".join([random.choice(POSSIBLE_CHARS) for _ in range(7)])
