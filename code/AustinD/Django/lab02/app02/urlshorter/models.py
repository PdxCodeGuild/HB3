from django.db import models
import random
import string

class Url(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=6))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.url} -> {self.code}"
