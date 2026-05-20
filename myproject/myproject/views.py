from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html')

def github(request):
    return render(request, 'github.html')
