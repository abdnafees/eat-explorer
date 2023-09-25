"""
This file contains URL endpoints for Restaurants app.
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from backend.restaurants.api.v1.views import RestaurantSearchView

urlpatterns = [
    path("", RestaurantSearchView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
