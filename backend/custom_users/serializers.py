"""
This file contains Serializer class for the Custom User model.
"""
from rest_framework import serializers

from backend.custom_users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}
