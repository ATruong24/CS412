'''
<!--
Description: Registers the models and help migrate
Author: Anthony Truong
Date: Fall 2026
-->
'''

from django.contrib import admin
from .models import Profile, Post, Photo

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)