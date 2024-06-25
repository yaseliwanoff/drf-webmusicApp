from django.contrib.auth.models import User
from rest_framework import serializers
from datetime import datetime
from .models import Artist, Album, Song


class UserSerializer(serializers.ModelSerializer):
    """
    Automatically sets a pk(id) field (ex: id: 1)
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


# class ArtistHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
#     """
#     Set a url field instead of a pk field
#     """
#     class Meta:
#         model = Artist
#         fields = '__all__'


class ArtistSerializator(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'  # all fields for serializers


class AlbumSerializator(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['__all__']  # all fields for serializers


class SongSerializator(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['__all__']  # all fields for serializers


# Serializers overview
# class Comment:
#     def __init__(self, email, content, created=None):
#         self.email = email
#         self.content = content
#         self.created = created or datetime.now()


# class CommentSerializers(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Comment(**validated_data)

#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('email', instance)
