# Generated by Django 3.0.2 on 2020-01-07 01:56

import conference_rooms.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference_rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(validators=[conference_rooms.validators.validate_date]),
        ),
    ]
