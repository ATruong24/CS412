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