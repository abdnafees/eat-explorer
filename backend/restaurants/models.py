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
    name = models.CharField(max_length=255)
    address = models.TextField()
    cuisine = models.CharField(max_length=100)
    price_range = models.CharField(max_length=20)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
