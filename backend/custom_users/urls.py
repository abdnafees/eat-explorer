"""
This file contains URL endpoints for Users app.
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from backend.custom_users.views import (
    UserProfileView,
    UsersListView,
    UserCreateView,
)

urlpatterns = [
    path("", UserCreateView.as_view()),
    path("list/", UsersListView.as_view(), name="list"),
    path("profile/", UserProfileView.as_view(), name="profile"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
