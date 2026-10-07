'''
Description: Displays different views and functions
Author: Anthony Truong
Date: Fall 2026
'''
from django.urls import reverse
from django.shortcuts import render
from .forms import CreatePostForm
from django.views.generic import ListView, DetailView, CreateView
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

class CreatePostView(CreateView):
    '''A view to create a new post and save to database'''
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context varaible'''
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        context['profile'] = profile
        return context

    def form_valid(self, form):
        '''Attaches profile to post, saves it, and create a photo for the new post'''
        print(f"CreatePostView.form_valid: form.cleaned_data={form.cleaned_data}")

        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        form.instance.profile = profile

        response = super().form_valid(form)
        image_url = self.request.POST.get('image_url')

        if image_url:
            photo = Photo(post=self.object, image_url=image_url)
            photo.save()

        return response

    def get_success_url(self):
        '''Provide a URL to redirect to after making a new post'''

        return reverse('show_post', kwargs={'pk': self.object.pk})