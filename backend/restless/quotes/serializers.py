from rest_framework import serializers
from .models import *

# class QuoteSerializer(serializers.ModelSerializer):
#     author = serializers.CharField(source='author.name')
#     class Meta:
#         model = Quotes
#         fields = ('id','quote','author')

class AuthorSerializer(serializers.Serializer):
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    name=serializers.CharField(max_length=100)
    class Meta:
        model = Author
        fields = ('id','name',)

    def create(self, validated_data):
        return Author.objects.create(**validated_data) 

class QuoteSerializer(serializers.ModelSerializer):
    quote=serializers.CharField(max_length=300)
    author=serializers.CharField(source='author.name')

    class Meta:
        model = Quotes
        fields = ('id','quote','author')
 
class AuthorQuoteSerializer(serializers.ModelSerializer):
    id=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Author
        fields = ("id",)

class QuotePostSerializer(serializers.ModelSerializer):
    author=serializers.StringRelatedField()
    class Meta:
        model = Quotes
        fields = ('quote','author')

    def create(self, validated_data):
        return Quotes.objects.create(**validated_data)