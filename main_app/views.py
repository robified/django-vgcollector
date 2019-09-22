from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse # Okay to delete this line because home is now rending a home.html
from .models import Videogame, Console
from .forms import PlaytimeForm

class VideogameCreate(LoginRequiredMixin, CreateView):
    model = Videogame
    # fields = '__all__'
    # Or you can do
    fields = ['name', 'genre', 'description', 'year']
    success_url = '/videogames/'
    # This inherited method is called when a valid videogame form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class VideogameUpdate(UpdateView):
    model = Videogame
    # Let's disallow the renaming of a video game by excluding the name field!
    fields = ['genre', 'description', 'year']

class VideogameDelete(LoginRequiredMixin, DeleteView):
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

class ConsoleList(LoginRequiredMixin, ListView):
    model = Console

class ConsoleDetail(LoginRequiredMixin, DetailView):
    model = Console

class ConsoleCreate(LoginRequiredMixin, CreateView):
    model = Console
    fields = '__all__'

class ConsoleUpdate(LoginRequiredMixin, UpdateView):
    model = Console
    fields = ['name', 'developer']

class ConsoleDelete(LoginRequiredMixin, DeleteView):
    model = Console
    success_url = '/consoles/'

# Create your views here.
def home(request):
    # return HttpResponse('<h1>Herro! /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def videogames_index(request):
    # This reads ALL videogames, not just the logged in user's videogames
    videogames = Videogame.objects.filter(user=request.user).order_by('name')
    # You could also retrieve the logged in user's videogames like this
    # videogames = request.user.videogames_set.all()
    return render(request, 'videogames/index.html', { 'videogames': videogames })

@login_required
def videogames_detail(request, videogame_id):
    videogame = Videogame.objects.get(id=videogame_id)
    # Get the consoles the videogame doesn't have
    consoles_videogame_doesnt_have = Console.objects.exclude(id__in = videogame.consoles.all().values_list('id'))
    # instantiate PlaytimeForm to be rendered in the template
    playtime_form = PlaytimeForm()
    return render(request, 'videogames/detail.html', { 
        # include the videogame and playtime_form in the context
        'videogame': videogame, 'playtime_form': playtime_form,
        # Add the toys to be displayed
        'consoles': consoles_videogame_doesnt_have
    })

@login_required
def add_playtime(request, videogame_id):
    # create the ModelForm using the data in request.POST
    form = PlaytimeForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it has the videogame_id assigned
        new_playtime = form.save(commit=False)
        new_playtime.videogame_id = videogame_id
        new_playtime.save()
    return redirect('detail', videogame_id=videogame_id)

def assoc_console(request, videogame_id, console_id):
    # Note that you can pass a console's id instead of the whole object
    Videogame.objects.get(id=videogame_id).consoles.add(console_id)
    return redirect('detail', videogame_id=videogame_id)

# add_photo

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)