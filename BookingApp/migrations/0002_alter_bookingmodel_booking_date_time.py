# Generated by Django 4.0.4 on 2022-05-22 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='booking_date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 22, 14, 5, 27, 834270)),
        ),
    ]
