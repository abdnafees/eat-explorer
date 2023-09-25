from rest_framework import serializers

from backend.restaurants.api.v1.models import Restaurant, Location, Photo, Geometry


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class GeometrySerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Geometry
        fields = "__all__"


class RestaurantSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)
    geometry = GeometrySerializer()

    class Meta:
        model = Restaurant
        fields = "__all__"
