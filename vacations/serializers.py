"""
Serializers for the Vacation API.

This module defines the serializers used to convert Vacation model instances
to and from JSON representations for use in the REST API.
"""

from rest_framework import serializers
from .models import Vacation


class VacationSerializer(serializers.ModelSerializer):
    """Serializer for the Vacation model, exposing all fields."""

    class Meta:
        model = Vacation
        fields = '__all__'
