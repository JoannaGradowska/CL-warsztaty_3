import datetime
from django.core.exceptions import ValidationError


def validate_date(date):
    if date < datetime.date.today():
        raise ValidationError("The date of reservation cannot be in the past!".format(date))