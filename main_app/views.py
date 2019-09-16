from django.shortcuts import render, redirect
# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the following import
# from django.http import HttpResponse # Okay to delete this line because home is now rending a home.html
from .models import Videogame
from .forms import PlaytimeForm

class VideogameCreate(CreateView):
    model = Videogame
    fields = '__all__'
    # Or you can do
    # fields = ['name', 'genre', 'description', 'year']
    success_url = '/videogames/'

class VideogameUpdate(UpdateView):
    model = Videogame
    # Let's disallow the renaming of a video game by excluding the name field!
    fields = ['genre', 'description', 'year']

class VideogameDelete(DeleteView):
    model = Videogame
    success_url = '/videogames/'

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
    videogames = Videogame.objects.order_by('name')
    return render(request, 'videogames/index.html', { 'videogames': videogames })

def videogames_detail(request, videogame_id):
    videogame = Videogame.objects.get(id=videogame_id)
    # instantiate PlaytimeForm to be rendered in the template
    playtime_form = PlaytimeForm()
    return render(request, 'videogames/detail.html', { 
        'videogame': videogame, 'playtime_form': playtime_form
    })

def add_playtime(request, videogame_id):
    # create the ModelForm using the data in request.POST
    form = PlaytimeForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it has the videogame_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.videogame_id = videogame_id
        new_feeding.save()
    return redirect('detail', videogame_id=videogame_id)