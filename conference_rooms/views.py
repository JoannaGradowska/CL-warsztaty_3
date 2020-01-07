from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from conference_rooms.forms import ReservationForm
from conference_rooms.models import Room, Reservation


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
        room = Room.objects.get(pk=pk)
        form = ReservationForm()
        return render(request, 'room_details.html', context={
            'room': room,
            'form': form,
        })

    def post(self, request, pk):
        form = ReservationForm(request.POST)
        room = Room.objects.get(pk=pk)
        if form.is_valid():
            reservation = Reservation()
            reservation.date = form.cleaned_data['date']
            reservation.comment = form.cleaned_data['comment']
            reservation.room_id = pk
            return self.checking_for_same_day_reservation(form, pk, request, reservation, room)
        else:
            return render(request, 'room_details.html', context={
                'room': room,
                'form': form,
            })

    @staticmethod
    def checking_for_same_day_reservation(form, pk, request, reservation, room):
        reservations_for_this_room = Reservation.objects.filter(room_id=pk)
        for res in reservations_for_this_room:
            if res.date == form.cleaned_data['date']:
                return render(request, 'room_details.html', context={
                    'room': room,
                    'form': form,
                    'end': f"You cannot make reservation for {Room.objects.get(pk=pk)} room on the {reservation.date}."})
        reservation.save()
        return redirect('/')


class RoomsView(View):
    def get(self, request):
        return render(request, 'rooms.html', context={
            'rooms': Room.objects.all()
        })
