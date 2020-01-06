from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from conference_rooms.models import Room


class RoomCreate(CreateView):
    model = Room
    fields = '__all__'
    success_url = '/room/new/'


class RoomModify(UpdateView):
    model = Room
    fields = '__all__'
    template_name_suffix = '_modify_form'
    success_url = '/room/new/'


class RoomDelete(DeleteView):
    model = Room
    success_url = '/room/new/'


class RoomDetails(View):
    def get(self, request, pk):
        return render(request, 'room_details.html', context={
            'room': Room.objects.get(pk=pk),
        })


class RoomsView(View):
    def get(self, request):
        return render(request, 'rooms.html', context={
            'rooms': Room.objects.all()
        })
