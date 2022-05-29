from urllib import request
from rest_framework import serializers

from .models import BookingModel
class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = BookingModel
        fields=["_id","booking_person_name","booking_person_address","booking_person_mobile","booking_date_time","owner","service"]

        
