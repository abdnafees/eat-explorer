"""
This file contains URL endpoints for Users app.
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from backend.user.api.v1.views import (
    UserRetrieveAPIView,
    UserListAPIView,
    UserCreateAPIView,
)

urlpatterns = [
    path("", UserCreateAPIView.as_view(), name="users"),
    path("", UserListAPIView.as_view(), name="users"),
    path("<int:id>", UserRetrieveAPIView.as_view(), name="detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
