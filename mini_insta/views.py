'''
Description: Displays different views and functions
Author: Anthony Truong
Date: Fall 2026
'''
from django.urls import reverse
from django.shortcuts import render
from django.db.models import Q
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile, Post, Photo
# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
import time
import random
from rest_framework import generics
from .serializers import ProfileSerializer, PostSerializer

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

class ShowFollowersDetailView(DetailView):
    '''Display the profiles who follow a profile'''

    model = Profile
    template_name = "mini_insta/show_followers.html"
    context_object_name = 'profile'

class ShowFollowingDetailView(DetailView):
    '''Display the profiles that a given profile follows'''

    model = Profile
    template_name = "mini_insta/show_following.html"
    context_object_name = 'profile'

class ShowFeedView(DetailView):
    '''Display the post feed for a single profile'''

    model = Profile
    template_name = "mini_insta/show_feed.html"
    context_object_name = 'profile'

class SearchView(ListView):
    '''Search profiles and post on the given profile. show the search form if no query was given'''

    template_name = "mini_insta/search_results.html"

    def dispatch(self, request, *args, **kwargs):
        '''Handle request, if there is no query, show search form otherwise continue with ListView processsing'''

        query = self.request.GET.get('query')
        if not query:
            # no query yet, show search form
            profile = Profile.objects.get(pk=kwargs['pk'])
            return render(request, "mini_insta/search.html", {'profile': profile})
        
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        ''' Returns queryset of posts whose caption contains the query'''

        query = self.request.GET.get('query')
        return Post.objects.filter(caption__icontains=query).order_by('-timestamp')

    def get_context_data(self, **kwargs):
        '''Return a dict of context variables for use in template'''

        context = super().get_context_data(**kwargs)

        # the profile on whose behalf we are searching
        pk = self.kwargs['pk']
        context['profile'] = Profile.objects.get(pk=pk)
        query = self.request.GET.get('query')
        context['query'] = query

        # the posts that match 
        context['posts'] = self.get_queryset()
        context['profiles'] = Profile.objects.filter(
            Q(username__icontains=query) |
            Q(display_name__icontains=query) |
            Q(bio_text__icontains=query)
        )

        return context

# ---------------- REST API views ----------------

class APIAuthMixin:
    '''Require a valid token for an API view'''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_user_profile(self):
        return Profile.objects.filter(user=self.request.user).first()


class LoginAPIView(APIView):
    '''API: check a username and password'''

    authentication_classes = []      
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid username or password.'},
                            status=status.HTTP_401_UNAUTHORIZED)

        profile = Profile.objects.filter(user=user).first()
        if profile is None:
            return Response({'error': 'This user has no profile.'},
                            status=status.HTTP_404_NOT_FOUND)

        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key,
                         'user_id': user.id,
                         'profile_id': profile.id})


class ProfileListAPIView(APIAuthMixin, generics.ListAPIView):
    '''API: return a list of all profiles as JSON'''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailAPIView(APIAuthMixin, generics.RetrieveAPIView):
    '''API: return one profile as JSON.'''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfilePostsAPIView(APIAuthMixin, generics.ListAPIView):
    '''API: return the posts of a profile'''
    serializer_class = PostSerializer

    def get_queryset(self):
        '''Return this profile's post'''
        return Post.objects.filter(profile__pk=self.kwargs['pk']).order_by('-timestamp')


class ProfileFeedAPIView(APIAuthMixin, generics.ListAPIView):
    '''API: return the feed for the logged in user profile'''
    serializer_class = PostSerializer

    def get_queryset(self):
        profile = self.get_user_profile()
        if profile is None or profile.pk != self.kwargs['pk']:
            raise PermissionDenied('You can only view your own feed.')
        return profile.get_post_feed()   # keep YOUR feed method name


class CreatePostAPIView(APIAuthMixin, generics.CreateAPIView):
    '''API: create a new Post'''
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(profile=self.get_user_profile())