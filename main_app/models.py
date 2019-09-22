from django.db import models
# Import the reverse function
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

# A tuple of 2-tuples
TIME_OF_DAY = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening'),
    ('N', 'Night')
)

# Create your models here.
class Console(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('consoles_detail', kwargs={'pk': self.id})

class Videogame(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=350)
    year = models.IntegerField()
    # Add the M:M relationship 
    consoles = models.ManyToManyField(Console)
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'videogame_id': self.id})
    
    def played_for_today(self):
        return self.playtime_set.filter(date=date.today()).count() >= len(TIME_OF_DAY)

class Playtime(models.Model):
    date = models.DateField('play date')
    time_of_day = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=TIME_OF_DAY,
        # set the default value for meal to be 'B'
        default=TIME_OF_DAY[3][0]
    )

    # Create a videogame_id FK
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_time_of_day_display()} on {self.date}"
    
    # change the default sort from lastest to oldest
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for videogame_id: {self.videogame_id} @{self.url}"