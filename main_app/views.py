from django.shortcuts import render
# Add the follwoing import
from django.http import HttpResponse

# Create your views here.
# Define the home view
def home(request):
    return HttpResponse('<h1>Herro! /ᐠ｡‸｡ᐟ\ﾉ Here\'s the video game collector homepage.</h1>')

def about(request):
    return render(request, 'about.html')