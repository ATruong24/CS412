'''
Description: Serializers to convert jokes into JSON
Author: Anthony Truong
Date: Fall 2026
'''

from rest_framework import serializers
from .models import Joke, Picture

class JokeSerializer(serializers.ModelSerializer):
    '''Serializer for the joke model and fields'''

    class Meta:
        model = Joke
        fields = ['id', 'text', 'added_by', 'timestamp']


class PictureSerializer(serializers.ModelSerializer):
    '''Serializer for the picture model and fields'''

    class Meta:
        model = Picture
        fields = ['id', 'image_url', 'added_by', 'timestamp']