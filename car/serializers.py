from rest_framework import serializers

from core.models import Car, Part



class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ["name", "price"]
        extra_kwargs = {
            'name': {'read_only': True},
            'price': {'read_only': True},
        }

class CarSerializer(serializers.ModelSerializer):
    part=PartSerializer(read_only=True,many=True)
    class Meta:
        model = Car
        fields = ["name", "car_model", "part"]
        extra_kwargs = {
            'name': {'read_only': True},
            'car_model': {'read_only': True},
            'part': {'read_only': True},

        }

