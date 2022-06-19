from django.shortcuts import get_object_or_404
from rest_framework import serializers

from core.models import Car


class ReceptionCreateCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        extra_kwargs = {
            'is_repaired': {'read_only': True},
            'is_finished': {'read_only': True},
            'part': {'read_only': True},

        }

    def create(self, validated_data):
        return Car.objects.create(**validated_data)



class ReceptionUpdateCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["name","car_model"]
