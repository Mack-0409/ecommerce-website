from django.shortcuts import render, redirect

# Create your views here.

def order_list(request):
    return render(request, 'order_success.html')

def order_details(request):
    return render(request, 'order_details.html')

def checkout(request):
    return render(request, 'checkout.html')