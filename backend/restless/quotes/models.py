from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=100)

class Quotes(models.Model):
    quote=models.CharField(max_length=300)
    author=models.ForeignKey(Author,related_name="quote_set" ,on_delete=models.CASCADE)
