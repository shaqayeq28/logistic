from rest_framework import serializers

from core.models import Car


class TechnicianRapairCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        extra_kwargs = {
            'name': {'read_only': True},
            'is_finished': {'read_only': True},
            'car_model': {'read_only': True},
            'part': {'read_only': True},

        }


class TechnicianAddPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        extra_kwargs = {
            'name': {'read_only': True},
            'is_finished': {'read_only': True},
            'car_model': {'read_only': True},
            'is_repaired': {'read_only': True},

        }
