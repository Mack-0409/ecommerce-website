from django.shortcuts import render

# Create your views here.

def cart(request):
    return render(request, 'cart.html')

def add_to_cart(request, pk):
    return render(request, 'cart.html')

def remove_from_cart(request, pk):
    return render(request, 'caart.html')