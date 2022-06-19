from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from car.serializers import CarSerializer
from core.models import Car,Part



class CarView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        qs = Car.objects.all()
        serializer = CarSerializer(qs, many=True)
        return Response(serializer.data)


class CarDetailView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]


class PartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        qs = Part.objects.all()
        serializer = CarSerializer(qs, many=True)
        return Response(serializer.data)
