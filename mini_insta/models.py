'''
Description: Models for profiles, post and pictures
Author: Anthony Truong
Date: Fall 2026
'''

from django.db import models
from django.utils import timezone

# Create your models here.


class Profile(models.Model):
    '''Models a single Instagram-like user profile.'''
    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Returns User's Username'''
        return f"{self.username} ({self.display_name})"

    def get_all_posts(self):
        '''Returns a Set of all posts of this profile'''
        return Post.objects.filter(profile=self).order_by('-timestamp')

class Post(models.Model):
    '''Models a single post made by a user profile'''
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        '''Returns a short description of post'''
        return f"Post by {self.profile.username} at {self.timestamp:%Y-%m-%d %H:%M}"

    def get_all_photos(self):
        '''Returns a set of all photos attached to the post'''
        return Photo.objects.filter(post=self).order_by('timestamp')




class Photo(models.Model):
    '''Mdoels a single image attached to a post'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Returns a short desciption of the photo'''
        if self.image_url:
            return f"Photo for post {self.post.pk}: {self.image_url}"
        else:
            return f"Photo for post {self.post.pk}: {self.image_file.name}"

    def get_image_url(self):
        '''Returns the URL of this photo's image'''
        if self.image_url:
            return self.image_url
        elif self.image_file:
            return self.image_file.url
        else:
            return ''
    