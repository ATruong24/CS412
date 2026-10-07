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