'''
Description: Models for dad jokes application
Author: Anthony Truong
Date: Fall 2026
'''

from django.db import models

class Joke(models.Model):
    '''Models a single dad joke'''

    text = models.TextField(blank=False)
    added_by = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return joke text and who contributed it'''
        return f"{self.text} (by {self.added_by})"


class Picture(models.Model):
    '''Models an image or GIF stored in a URL'''

    image_url = models.URLField(blank=False)
    added_by = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return the image URL and who contributed it'''
        return f"{self.image_url} (by {self.added_by})"