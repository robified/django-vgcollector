from django.shortcuts import render
# Add the follwoing import
# from django.http import HttpResponse # Okay to delete this line because home is now rending a home.html
from .models import Videogame

# # Add the Video Game class & list and view function below the imports
# class Videogame: # Note that parens are optional if not inheriting from another class
#     def __init__(self, name, genre, description, year):
#         self.name = name
#         self.genre = genre
#         self.description = description
#         self.year = year

# videogames = [
#     Videogame('Street Fighter 3rd Strike', 'Fighting game', 'a 2D fighting game developed and published by Capcom.', 1999),
#     Videogame('Bayonetta', 'Action, hack and slash', 'an action-adventure hack and slash video game developed by PlatinumGames and published by Sega.', 2009),
#     Videogame('The Legend of Zelda: A Link to the Past', 'Action-adventure', 'an action-adventure game developed and published by Nintendo.', 1991)
# ]

# Create your views here.
# Define the home view
def home(request):
    # return HttpResponse('<h1>Herro! /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Add new view
def videogames_index(request):
    videogames = Videogame.objects.all()
    return render(request, 'videogames/index.html', { 'videogames': videogames })