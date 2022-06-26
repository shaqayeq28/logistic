from django.shortcuts import render
from rest_framework.generics import UpdateAPIView
from core.models import Car
from inspector.serializers import InspectorSerializer
from core.permissions import IsInspector

# Create your views here.



class IsFinished(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = InspectorSerializer
    permission_classes = [IsInspector]
