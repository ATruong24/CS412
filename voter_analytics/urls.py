'''
Description: Views file for URL Patterns
Author: Anthony Truong
Date: Fall 2026
'''

from django.urls import path
from django.conf import settings
from . import views
 
 
urlpatterns = [
    path('', views.VoterListView.as_view(), name='voters'),
    path('voter/<int:pk>', views.VoterDetailView.as_view(), name='voter'),
    path('graphs', views.GraphsListView.as_view(), name='graphs'),
]