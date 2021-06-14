from django.db import models
import requests
# Create your models here.

class Url(models.Model):
    link = models.URLField(unique=True)

    def __str__(self):
        return self.link


    @property
    def status_code(self):
        return requests.get(self.link).status_code