from dataclasses import fields
from rest_framework import serializers
from .models import ServiceModel
class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceModel
        fields=["_id","service_name","service_description","is_active"]
