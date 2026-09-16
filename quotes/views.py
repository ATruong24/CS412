from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random

def home(request):
    '''
    Define a view to handle the 'home' request.
    '''
 
 
    response_text = '''
    <html>
    <h1>Hello, world!</h1>
 
 
    </html>
    '''
    
    return HttpResponse(response_text)

# Picutres Links Below

QUOTES = [
    "Embarrassment is where growth happens.",
    "Before you can lead anybody else, you gotta put yourself in the right position to be successful",
    "I want to understand everything so I can put myself in a position to be successful",
    "Fearlessness is contagious"
]

IMAGES = [
    "https://cdn.nba.com/headshots/nba/latest/1040x760/1627759.png",
    "https://media.cnn.com/api/v1/images/stellar/prod/230726181303-jaylen-brown-file-052923-restricted.jpg?c=original",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTD4T5Z5g_HgOsr3YIIb6KxBXL0o7d3kCZ0RWcQ31Y3Kn59YTv-2R-G1uKN&s=10",
    "https://media.thecrimson.com/photos/2018/03/01/233239_1328650.jpg"
]

def quote(request):
    selected_quote = random.choice(QUOTES)
    selected_image = random.choice(IMAGES)

    context = {
        'quote': selected_quote,
        'image': selected_image,
    }
    return render(request, 'quotes/quote.html', context)

def show_all(request):

    context = {
        'quotes': QUOTES,
        'images': IMAGES,
    }
    return render(request, 'quotes/show_all.html', context)

def about(request):
    return render(request, 'quotes/about.html')

def home_page(request):
    '''Define a view to show the 'home.html' template.'''
 
 
    # the template to which we will delegate the work
    template = 'hw/home.html'
 
 
    # a dict of key/value pairs, to be available for use in template
    context = {
        'current_time': time.ctime(),
    }
 
 
    return render(request, template, context)