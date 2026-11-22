'''
Description: Serializers that convert mini_insta models to and from JSON for the REST API
Author: Anthony Truong
Date: Fall 2026
'''
from rest_framework import serializers
from .models import Profile, Post, Photo


class PhotoSerializer(serializers.ModelSerializer):
    '''Convert photo to JSON'''

    class Meta:
        model = Photo
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    '''Convert a Post to JSON'''

    # include each post's photos inside the post's JSON
    photos = PhotoSerializer(source='photo_set', many=True, read_only=True)
    username = serializers.CharField(source='profile.username', read_only=True)


    class Meta:
        model = Post
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    '''Convert a profile to JSON'''

    class Meta:
        model = Profile
        fields = '__all__'