from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views as auth_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookings/', include("BookingApp.urls")),
    path("auth-token/",auth_token.obtain_auth_token),
    path("services/",include("ServiceApp.urls"))
    
]
