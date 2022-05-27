from operator import truediv
from django.http import JsonResponse
from rest_framework.decorators import APIView
from .models import ServiceModel
from .ServiceSerializer import ServiceSerializer
from BookingApp.BookingExceptionHandler import NOT_FOUND
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly
from rest_framework.parsers import JSONParser

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        if(request.method in SAFE_METHODS):
            return True
        else:
            return False


class ServiceController(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser | ReadOnly]

    def get(self, request, format=None):
        services = ServiceModel.objects.all()
        if(len(services) != 0):
            serializer = ServiceSerializer(services, many=True)
        else:
            raise NOT_FOUND(detail="NOT FOUND", code=404)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self,request,format=None):
        data = JSONParser().parse(request)

        serializer = ServiceSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED,safe=False)
        else:
            return  JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
