'''
Description: Displays different views and functions
Author: Anthony Truong
Date: Fall 2026
'''

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile, Post, Photo
# Create your views here.
from django.http import HttpRequest, HttpResponse
import time
import random

class ProfileListView(ListView):
    """Displays all Profiles"""
    model = Profile
    template_name = 'mini_insta/show_all_profiles.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):
    """Displays a single Profile"""
    model = Profile
    template_name = 'mini_insta/show_profile.html'
    context_object_name = 'profile'

class PostDetailView(DetailView):
    '''Displays a single Post and all the photos'''
    model = Post
    template_name = 'mini_insta/show_post.html'
    context_object_name = 'post'


