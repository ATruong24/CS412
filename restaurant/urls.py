# Description: URL routing for restaurant application. Main, Order, and Confirmation
# Author: Anthony Truong
# Date: Fall 2026

from django.urls import path
from django.conf import settings
from . import views
 
 
urlpatterns = [
    # Routes to main restaurant information page
    path('main', views.main, name='main'),
    # Routes to the order form page
    path('order', views.order, name='order'),
    # Routes to the form submission confirmation page
    path('confirmation', views.confirmation, name='confirmation'),
]