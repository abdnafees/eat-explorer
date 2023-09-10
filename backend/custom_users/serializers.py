"""
This file contains Serializer class for the Custom User model.
"""
from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class CustomUserLoginSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ["username", "password"]
