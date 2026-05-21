from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')


