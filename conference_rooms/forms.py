from django.forms import ModelForm, DateInput
from conference_rooms.models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        exclude = ['room']
        widgets = {
            'date': DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'})
        }