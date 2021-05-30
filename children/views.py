from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, 'main/index.html')

def login(request):
    return render(request, 'authentication/login.html')

def register(request):
    return render(request, 'authentication/signup.html')

