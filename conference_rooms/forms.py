from django.forms import ModelForm

from conference_rooms.models import Room, Reservation


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
