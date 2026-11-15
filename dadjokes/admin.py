'''
<!--
Description: Registers the models and help migrate
Author: Anthony Truong
Date: Fall 2026
-->
'''

from django.contrib import admin
from .models import Joke, Picture

# Register your models here.
admin.site.register(Joke)
admin.site.register(Picture)