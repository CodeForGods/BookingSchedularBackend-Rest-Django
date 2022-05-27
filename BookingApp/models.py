from datetime import datetime
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

from ServiceApp.models import ServiceModel

class BookingModel(models.Model):
    _id = models.IntegerField(primary_key=True)
    booking_person_name = models.CharField(max_length=1000)
    booking_person_address = models.TextField(max_length=20000)
    booking_person_mobile = models.CharField(max_length=1000)
    booking_date_time = models.DateTimeField(default=datetime.now())
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    service = models.ForeignKey(ServiceModel,on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.booking_person_name




