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
    return render(request, 'restaurant/main.html')


def order(request):
    context = {
        'daily_special' : random.choice(daily_special)
    }
    return render(request, 'restaurant/order.html', context)


def confirmation(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        instructions = request.POST.get('instructions')
        ordered_items = request.POST.getlist('items')

        menu = {
            'Cheese Pizza': 18.00,
            'Pepporoni Pizza': 22.00,
            'Wings': 9.00,
            '2 Liter Soda': 3.00,
            'Cheesecake': 4.50,
            'Daily Special': 20.00,
        }

        total_price = 0
        for item in ordered_items:
            if item in menu:
                total_price += menu[item]

        daily_special = request.POST.get('daily_special')
        if daily_special:
            total_price += 20.00
            ordered_items.append(f"Special: {daily_special}")

        extra_meat = request.POST.get('extra_meat')
        if extra_meat and extra_meat != "None":
            total_price += 3.00
            ordered_items.append(f"Extra Option: {extra_meat}")

        
        ready_time = time.strftime("%I:%M %p %Z", time.localtime(time.time() + (20 * 60)))

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

    return render(request, 'restaurant/order.html')

