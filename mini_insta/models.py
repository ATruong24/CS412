'''
Description: Models for profiles, post and pictures
Author: Anthony Truong
Date: Fall 2026
'''

from django.db import models
from django.utils import timezone
from django.urls import reverse
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

    def get_absolute_url(self):
        '''Return the URL to display the profile'''
        return reverse('show_profile', kwargs={'pk': self.pk})
    
    def get_followers(self):
        '''Return a list of profiles who follow this profile'''
        follows = Follow.objects.filter(profile=self)
        return [follow.follower_profile for follow in follows]

    def get_num_followers(self):
        '''Return the number of profiles who follow this profile'''
        return len(self.get_followers())

    def get_following(self):
        '''Return a list of profiles that this profile follows.'''
        follows = Follow.objects.filter(follower_profile=self)
        return [follow.profile for follow in follows]

    def get_num_following(self):
        '''Return the number of profiles this profile follows'''
        return len(self.get_following())

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

    def get_all_comments(self):
        '''Return a queryset of all comments on this post by oldest first'''
        return Comment.objects.filter(post=self).order_by('timestamp')

    def get_likes(self):
        '''Return a set of all likes on this post'''
        return Like.objects.filter(post=self)

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

class Follow(models.Model):
    '''Model one profile following another profile'''

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile")
    follower_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="follower_profile")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string shwoing who follows whom'''
        return f"{self.follower_profile.display_name} follows {self.profile.display_name}"

class Comment(models.Model):
    '''Models a profile commenting on a post'''

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=False)

    def __str__(self):
        '''Return a string showing who had commented and their comment'''
        return f"{self.profile.username} on post {self.post.pk}: {self.text}"


class Like(models.Model):
    '''Models one profile liking a post'''

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string showing who liked which post'''
        return f"{self.profile.username} likes post {self.post.pk}"
    