from .models import *
from rest_framework import serializers
from rest_framework.response import Response


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'name',)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance


class QuotesSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name')

    class Meta:
        model = Quotes
        fields = ('id', 'quote', 'author')


class QuotesCUDSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        source='author',
        queryset=Author.objects.all()
    )
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Quotes
        fields = [
            "quote",
            "author_id",
            "author",
        ]
