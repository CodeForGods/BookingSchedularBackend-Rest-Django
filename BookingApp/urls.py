from django.urls import path
from .views import BookingController

urlpatterns = [
    path("myBookings/<int:pk>", BookingController.as_view()),
   
]
