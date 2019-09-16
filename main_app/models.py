from django.db import models
# Import the reverse function
from django.urls import reverse

# A tuple of 2-tuples
TIME_OF_DAY = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening'),
    ('N', 'Night')
)

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