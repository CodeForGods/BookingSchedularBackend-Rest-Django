# Generated by Django 4.0.4 on 2022-05-22 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingApp', '0003_bookingmodel_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='booking_date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 22, 15, 25, 27, 50415)),
        ),
    ]
