from django.contrib import admin
# import your models here
from .models import Videogame, Playtime, Photo

# Register your models here.
admin.site.register(Videogame)
# Register the new Playtime model
admin.site.register(Playtime)
admin.site.register(Photo)