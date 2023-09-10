"""'
A model is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you're storing.
Generally, each model maps to a single database table.

The basics:

Each model is a Python class that subclasses django.db.models.Model.
Each attribute of the model represents a database field.
With all of this, Django gives you an automatically-generated database-access API; see Making queries.
"""
from django.db import models

# Create your models here.
# restaurants/models.py


class Restaurant(models.Model):
    name = models.CharField(max_length=255)  # Name of the restaurant
    place_id = models.CharField(
        max_length=255, unique=True
    )  # Unique identifier for the restaurant
    address = models.TextField()  # Address of the restaurant
    latitude = models.DecimalField(
        max_digits=10, decimal_places=6
    )  # Latitude of the restaurant's location
    longitude = models.DecimalField(
        max_digits=10, decimal_places=6
    )  # Longitude of the restaurant's location
    rating = models.FloatField(
        null=True, blank=True
    )  # Rating of the restaurant (can be nullable)
    user_ratings_total = models.PositiveIntegerField(
        null=True, blank=True
    )  # Total number of user ratings (can be nullable)
    price_level = models.PositiveIntegerField(
        null=True, blank=True
    )  # Price level of the restaurant (can be nullable)
    types = models.JSONField()  # List of restaurant types or categories
    photo_reference = models.CharField(
        max_length=255, null=True, blank=True
    )  # Reference to a restaurant's photo
    open_now = models.BooleanField(
        default=False
    )  # Indicates if the restaurant is open now

    def __str__(self):
        return self.name
