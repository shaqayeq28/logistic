from rest_framework import serializers

from core.models import Car


class InspectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        extra_kwargs = {
            'name': {'read_only': True},
            'car_model': {'read_only': True},
            'is_repaired': {'read_only': True},
            'part': {'read_only': True}

        }
