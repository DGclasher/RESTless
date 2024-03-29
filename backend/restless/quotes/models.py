from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    high_auth = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Quotes(models.Model):
    quote = models.CharField(max_length=300)
    author = models.ForeignKey(
        Author, related_name="quote_set", on_delete=models.CASCADE)
    high_auth_quote = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
