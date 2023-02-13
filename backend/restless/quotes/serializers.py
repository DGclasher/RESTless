from rest_framework import serializers
from rest_framework.response import Response
from .models import *


class QuotesSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name')

    class Meta:
        model = Quotes
        fields = ('id', 'quote', 'author')


class AuthorSerializer(serializers.ModelSerializer):
    quotes_author = QuotesSerializer(read_only=True, many=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'quotes_author')

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance
