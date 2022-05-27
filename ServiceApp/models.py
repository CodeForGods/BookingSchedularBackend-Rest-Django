from django.db import models


class ServiceModel(models.Model):

    _id = models.IntegerField(primary_key=True)
    service_name = models.CharField(max_length=1000)
    service_description = models.TextField(max_length=10000)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.service_name
