from django.views.generic import CreateView
from conference_rooms.models import Room


class RoomCreateView(CreateView):
    model = Room
    fields = '__all__'
    success_url = '/room/new/'
