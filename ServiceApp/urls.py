from django.urls import path

from .views import ServiceController
urlpatterns = [
    
    path("servicesList/",ServiceController.as_view())

]