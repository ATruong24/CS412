from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile
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