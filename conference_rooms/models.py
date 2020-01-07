from django.db import models

from conference_rooms.validators import validate_date


class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.IntegerField()
    projector = models.BooleanField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    date = models.DateField(validators=[validate_date])
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
