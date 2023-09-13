from django.contrib.gis.db import models


class Location(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)


class Geometry(models.Model):
    location = models.OneToOneField(Location, on_delete=models.CASCADE)


class Photo(models.Model):
    height = models.PositiveIntegerField()
    html_attributions = models.TextField()
    photo_reference = models.CharField(max_length=255)
    width = models.PositiveIntegerField()


class Restaurant(models.Model):
    name = models.CharField(max_length=255)  # Name of the restaurant
    geometry = models.OneToOneField(Geometry, on_delete=models.CASCADE)
    # Geometry information including latitude and longitude
    icon = models.URLField()  # URL to the restaurant's icon
    icon_background_color = models.CharField(
        max_length=7
    )  # Background color of the icon
    photos = models.ManyToManyField(Photo)  # Field to store photos information
    place_id = models.CharField(
        max_length=255, unique=True
    )  # Unique identifier for the restaurant
    rating = models.DecimalField(
        max_digits=3, decimal_places=1
    )  # Rating of the restaurant (decimal)
    reference = models.CharField(max_length=255)  # Reference to the restaurant
    types = (
        models.JSONField()
    )  # JSON field to store types (e.g., restaurant, food, point_of_interest)
    user_ratings_total = models.IntegerField()  # Total user ratings for the restaurant
    vicinity = models.TextField()  # Address or vicinity of the restaurant
    business_status = models.CharField(
        max_length=50
    )  # Business status of the restaurant (e.g., OPERATIONAL)

    def __str__(self):
        return self.name
