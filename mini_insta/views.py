'''
Description: Displays different views and functions
Author: Anthony Truong
Date: Fall 2026
'''
from django.urls import reverse
from django.shortcuts import render
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
        files = self.request.FILES.getlist('files')
        print(f"CreatePostView.form_valid: files={files}")


        for file in files:
            photo = Photo(post=self.object, image_file=file)
            photo.save()

        return response

    def get_success_url(self):
        '''Provide a URL to redirect to after making a new post'''

        return reverse('show_post', kwargs={'pk': self.object.pk})

class UpdateProfileView(UpdateView):
    '''A view to update an existing profile and save it to the database'''

    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"

class DeletePostView(DeleteView):
    '''A view to delete a post and remove it from the DB'''

    model = Post
    template_name = "mini_insta/delete_post_form.html"

    def get_context_data(self, **kwargs):
        '''Return dictionary of context variables for usin template'''

        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)

        # Add the post and its profile to dict
        context['post'] = post
        context['profile'] = post.profile
        return context

    def get_success_url(self):
        '''Return th eURL to redirect after successful delete'''

        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        profile = post.profile

        return reverse('show_profile', kwargs={'pk': profile.pk})

class UpdatePostView(UpdateView):
    '''A view to update the caption of an existing post'''

    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def get_success_url(self):
        '''Return the URL to redirect after a successful update'''

        return reverse('show_post', kwargs={'pk': self.object.pk})


