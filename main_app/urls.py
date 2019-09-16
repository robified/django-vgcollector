from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for video games index
    path('videogames/', views.videogames_index, name='index'),
    path('videogames/<int:videogame_id>/', views.videogames_detail, name='detail'),
    # new route used to show a form and create a videogame
    path('videogames/create/', views.VideogameCreate.as_view(), name='videogames_create'),
]