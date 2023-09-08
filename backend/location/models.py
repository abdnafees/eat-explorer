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


class Location(models.Model):
    name = models.CharField(max_length=255)  # Name of the location (e.g., city name)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6
    )  # Latitude (e.g., 40.7128)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6
    )  # Longitude (e.g., -74.0060)
    description = models.TextField(
        blank=True, null=True
    )  # Description or additional information about the location

    def __str__(self):
        return self.name
