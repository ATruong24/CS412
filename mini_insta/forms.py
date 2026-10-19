'''
Description: Forms for the mini_insta application
Author: Anthony Truong
Date: Fall 2026
'''

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    '''A form to create a new Post.'''

    class Meta:
        '''Associates this form with the post model'''
        model = Post
        fields = ['caption']

class UpdateProfileForm(forms.ModelForm):
    '''A form to update an existing Profile'''

    class Meta:
        '''Associate this form with the Profile model with select fields'''
        model = Profile
        fields = [
            'display_name',
            'profile_image_url',
            'bio_text'
        ]

class UpdatePostForm(forms.ModelForm):
    '''A form to update the caption of an existing post'''

    class Meta:
        '''Associate the form with Post model'''
        model = Post
        fields = ['caption']