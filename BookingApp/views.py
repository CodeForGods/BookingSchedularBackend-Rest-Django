from http.client import HTTPResponse
import imp
from .BookingExceptionHandler import NOT_FOUND,NOT_AUTHORIZED,Bad_Request
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import APIView
from BookingApp.models import BookingModel
from .BookingSerializer import BookingSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from rest_framework import status
from ServiceApp.models import ServiceModel

class IsOwner(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class BookingController(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner, IsAuthenticated]

    def get(self, request, pk, format=None):
        
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NOT_FOUND(detail="User Not Found", code=404)
        bookings = BookingModel.objects.filter(owner=user)
        if(len(bookings) == 0):
            raise NOT_FOUND(detail="NO Bookings Found", code=404)
        self.check_object_permissions(self.request, bookings[0])
        serializer = BookingSerializer(bookings, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self,request,pk,format=None):
        data = JSONParser().parse(request)
        
        serializer = BookingSerializer(data = data)
        if(serializer.is_valid()):          
            if(request.user.id!=int(data["owner"])):
                raise NOT_AUTHORIZED("NOT AUTHORIZED")
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)

        
        



