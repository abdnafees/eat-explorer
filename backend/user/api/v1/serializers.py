"""
This file contains Serializer class for the Custom User model.
"""
from rest_framework import serializers

from backend.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}
