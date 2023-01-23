from django.db import models

class Quotes(models.Model):
    quote=models.CharField(max_length=300)
    author=models.CharField(max_length=100)

