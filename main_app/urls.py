from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for video games index
    path('videogames/', views.videogames_index, name='index'),
    path('videogames/<int:videogame_id>/', views.videogames_detail, name='detail'),
    path('videogames/<int:videogame_id>/add_playtime/', views.add_playtime, name='add_playtime'),
    # new route used to show a form and create a videogame
    path('videogames/create/', views.VideogameCreate.as_view(), name='videogames_create'),
    path('videogames/<int:pk>/update/', views.VideogameUpdate.as_view(), name='videogames_update'),
    path('videogames/<int:pk>/delete/', views.VideogameDelete.as_view(), name='videogames_delete'),
    # crud routes for consoles
    path('consoles/', views.ConsoleList.as_view(), name='consoles_index'),
    path('consoles/<int:pk>/', views.ConsoleDetail.as_view(), name='consoles_detail'),
    path('consoles/create/', views.ConsoleCreate.as_view(), name='consoles_create'),
    path('consoles/<int:pk>/update/', views.ConsoleUpdate.as_view(), name='consoles_update'),
    path('consoles/<int:pk>/delete/', views.ConsoleDelete.as_view(), name='consoles_delete'),
    path('accounts/signup', views.signup, name='signup'),
    # associate a console with a videogame (M:M)
    path('videogames/<int:videogame_id>/assoc_console/<int:console_id>/', views.assoc_console, name='assoc_console'),
]