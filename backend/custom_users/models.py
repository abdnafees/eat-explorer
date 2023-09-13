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

    def create_user(self, email, username, password=None):
        if not username:
            raise ValueError("User must have a unique username.")

        user = self.model(email=self.normalize_email(email), username=username)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(PermissionsMixin, AbstractBaseUser):
    """This class defines fields for CustomUser model."""

    email = models.EmailField(unique=True)
    username = models.CharField(verbose_name="username", max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Add your custom fields here as needed

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
