"""
This file contains URL endpoints for Users app.
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserProfileView, UsersListView, UserLoginView, UserCreateView

urlpatterns = [
    path("", UsersListView.as_view()),
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("profile/", UserProfileView.as_view(), name="profile"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
