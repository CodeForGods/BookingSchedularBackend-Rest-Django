from .BookingExceptionHandler import NOT_FOUND
from django.http import JsonResponse
from rest_framework.decorators import APIView
from BookingApp.models import BookingModel
from .BookingSerializer import BookingSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission,SAFE_METHODS
from rest_framework import permissions
class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class BookingController(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, pk, format=None):
        try:
            bookings = BookingModel.objects.get(pk=pk)
        except:
            raise NOT_FOUND(detail="NOT FOUND",code=404)
        serializer = BookingSerializer(bookings)
        self.check_object_permissions(self.request,bookings)
        return JsonResponse(serializer.data,safe=False)
