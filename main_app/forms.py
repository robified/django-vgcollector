from django.forms import ModelForm
from .models import Playtime

class PlaytimeForm(ModelForm):
    class Meta:
        model = Playtime
        fields = ['date', 'time_of_day']