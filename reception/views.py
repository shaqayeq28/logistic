from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.views import APIView
from core.permissions import  IsReception

from core.models import Car
from reception.serializers import ReceptionCreateCarSerializer

from reception.serializers import ReceptionUpdateCarSerializer


class CarCreateView(APIView):
    permission_classes = [IsReception]

    def post(self, request: Request):
        qs = Car.objects.all()
        serializer = ReceptionCreateCarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

class CarUpdate(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = ReceptionUpdateCarSerializer
    permission_classes = [IsReception]
