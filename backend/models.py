"""'
A model is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you're storing.
Generally, each model maps to a single database table.

The basics:

Each model is a Python class that subclasses django.db.models.Model.
Each attribute of the model represents a database field.
With all of this, Django gives you an automatically-generated database-access API; see Making queries.
"""

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone

# Create your models here in models.py in your app


class CustomUserManager(BaseUserManager):
    """This class base function for creating a Custom User model."""

    def create_user(self, validated_data):
        if not validated_data["email"]:
            raise ValueError("The Email field must be set")
        if not validated_data["username"]:
            raise ValueError("User must have a unique username.")
        email = self.normalize_email(validated_data["email"])
        user = self.model(
            email=email,
            username=validated_data["username"],
        )
        user.set_password(validated_data["password"])
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """This class defines fields for CustomUser model."""

    email = models.EmailField(unique=True)
    username = models.CharField(verbose_name="username", max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    # Add your custom fields here as needed

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True
