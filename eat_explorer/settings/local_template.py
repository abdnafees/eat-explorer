"""
SECURITY WARNING: don't run with debug turned on in production!
"""

# noinspection PyUnresolvedReferences
from base import *

SECRET_KEY = "your_secret_key"

GOOGLE_MAPS_API_KEY = "your_google_maps_api_key"

DEBUG = True
ALLOWED_HOSTS = ["*"]

DJANGO_SETTINGS_MODULE = "eat_explorer.settings.local"

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "db_name",  # Choose a name for your database
        "USER": "db_user",  # Choose a username
        "PASSWORD": "db_password",  # Choose a password
        "HOST": "localhost",  # Change to your PostgreSQL host if necessary
        "PORT": "5432",  # Use the default PostgreSQL port
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]
