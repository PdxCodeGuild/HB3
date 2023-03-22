from django.db import models
import string
import random


# Create your models here.

code_characters = string.ascii_letters + string.digits

class Shortener(models.Model):
    url_long = models.URLField()
    random_code = models.CharField(primary_key=True, max_length=5, editable=False)

    def generate_code(self):
        self.random_code = "".join([random.choice(code_characters) for _ in range(5)])
    