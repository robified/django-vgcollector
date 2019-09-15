from django.db import models

# Create your models here.
class Videogame(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=350)
    year = models.IntegerField()

    # new code below
    def __str__(self):
        return self.name