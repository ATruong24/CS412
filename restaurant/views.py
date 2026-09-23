# restaurant/views.py
# Description: Handles the logic and data processing for the pizzeria web application. Holds function to calculate total and handle POST request.
# Author: Anthony Truong
# Date: Fall 2026

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random

daily_special = [
    "Meat Lover Pizza",
    "Detroit Pizza",
    "Lazagna"
]

def main(request):
    """
    Displays restaurant information page
    """
    return render(request, 'restaurant/main.html')


def order(request):

    """
    Displays order form to user. Chooses a random daily special list and passes the special item via context
    """
    # Generate a random special from the daily_special
    context = {
        'daily_special' : random.choice(daily_special)
    }
    return render(request, 'restaurant/order.html', context)


def confirmation(request):
    """
    Processes POST request from order form. Calculates total price of all items and handles optional add-ons and different requests,
    Generates random pickup time and gives confirmation receipt
    """
    # Process data once user submitted form
    if request.method == 'POST':
        # Retrieves data
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        instructions = request.POST.get('instructions')
        ordered_items = request.POST.getlist('items')

        # List of available items in restaurant and price
        menu = {
            'Cheese Pizza': 18.00,
            'Pepporoni Pizza': 22.00,
            'Wings': 9.00,
            '2 Liter Soda': 3.00,
            'Cheesecake': 4.50,
            'Daily Special': 20.00,
        }

        # Calculates the total price of the order
        total_price = 0
        for item in ordered_items:
            if item in menu:
                total_price += menu[item]

        # Grabs daily special if user requests it
        daily_special = request.POST.get('daily_special')
        if daily_special:
            total_price += 20.00
            ordered_items.append(f"Special: {daily_special}")

        # Ability to choose extra meat if user request it
        extra_meat = request.POST.get('extra_meat')
        if extra_meat and extra_meat != "None":
            total_price += 3.00
            ordered_items.append(f"Extra Option: {extra_meat}")

        # Gets random pickup time order will be available
        ready_time = time.strftime("%I:%M %p %Z", time.localtime(time.time() + (20 * 60)))

        # Pack content for template
        context = {
            'name' : name,
            'phone' : phone,
            'email' : email,
            'instructions' : instructions,
            'ready_time' : ready_time,
            'total_price': total_price,
            'ordered_items': ordered_items,
        }

        return render(request, 'restaurant/confirmation.html', context)
    # Redirect user to order page if they get here via GET request
    return render(request, 'restaurant/order.html')

