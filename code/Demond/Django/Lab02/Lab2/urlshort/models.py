from django.db import models
import string
import random

code_characters = string.ascii_letters + string.digits

# Create your models here.
class shortener(models.Model):
    code = models.CharField(max_length=6, primary_key=True, editable=False)
    url = models.URLField()
    def generate_code(self):
        self.code = "".join([random.choice(code_characters) for _ in range(6)])