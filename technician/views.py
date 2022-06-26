from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.views import APIView
from core.permissions import IsTechnician

from core.models import Car
from technician.serializers import TechnicianRepairCarSerializer, TechnicianAddPartSerializer


# Create your views here.


class RepairUpdate(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = TechnicianRepairCarSerializer
    permission_classes = [IsTechnician]


class AddPart(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = TechnicianAddPartSerializer
    permission_classes = [IsTechnician]


class RemovePart(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = TechnicianAddPartSerializer
    permission_classes = [IsTechnician]
