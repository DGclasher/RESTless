from rest_framework import serializers
from .models import *

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ('name',)

class QuoteSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name')
    class Meta:
        model = Quotes
        fields = ('id','quote','author')
