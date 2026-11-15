'''
Description: Displays different views and functions
Author: Anthony Truong
Date: Fall 2026
'''

import random
from django.views.generic import ListView, DetailView, TemplateView
from .models import Joke, Picture
from .serializers import JokeSerializer, PictureSerializer
from django.shortcuts import render
from rest_framework import generics


# Create your views here.

class RandomView(TemplateView):
    '''Display one joke and one picture at random'''

    template_name = "dadjokes/random.html"

    def get_context_data(self, **kwargs):
        '''Add a random joke and a random picture to context'''
        context = super().get_context_data(**kwargs)
        context['joke'] = Joke.objects.order_by('?').first()
        context['picture'] = Picture.objects.order_by('?').first()
        return context


class JokeListView(ListView):
    '''Display all jokes'''

    model = Joke
    template_name = "dadjokes/show_all_jokes.html"
    context_object_name = 'jokes'


class JokeDetailView(DetailView):
    '''Display one joke as primary key'''

    model = Joke
    template_name = "dadjokes/show_joke.html"
    context_object_name = 'joke'


class PictureListView(ListView):
    '''Display all pictures'''

    model = Picture
    template_name = "dadjokes/show_all_pictures.html"
    context_object_name = 'pictures'


class PictureDetailView(DetailView):
    '''Display one picture as primary key'''

    model = Picture
    template_name = "dadjokes/show_picture.html"
    context_object_name = 'picture'


class JokeListAPIView(generics.ListCreateAPIView):
    '''API view to list all Jokes and create a Joke'''

    queryset = Joke.objects.all()
    serializer_class = JokeSerializer


class JokeDetailAPIView(generics.RetrieveAPIView):
    '''API view to return a joke by primary key'''

    queryset = Joke.objects.all()
    serializer_class = JokeSerializer


class RandomJokeAPIView(generics.RetrieveAPIView):
    '''API view to return one joke at random'''

    serializer_class = JokeSerializer

    def get_object(self):
        return Joke.objects.order_by('?').first()


class PictureListAPIView(generics.ListAPIView):
    '''API view to list all pictures'''

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PictureDetailAPIView(generics.RetrieveAPIView):
    '''API view to return one picture by PK'''

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class RandomPictureAPIView(generics.RetrieveAPIView):
    '''API view to return one picture at random'''

    serializer_class = PictureSerializer

    def get_object(self):
        '''Return a random picture instead of PK'''
        return Picture.objects.order_by('?').first()