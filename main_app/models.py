from django.db import models
# Import the reverse function
from django.urls import reverse

# Create your models here.
class Videogame(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=350)
    year = models.IntegerField()

    # new code below
    def __str__(self):
        return self.name
    
    # add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'videogame_id': self.id})