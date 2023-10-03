"""
SECURITY WARNING: don't run with debug turned on in production!
"""
# noinspection PyUnresolvedReferences
from base import *

SECRET_KEY = "django-insecure-oj^&l(rn@%!#c*(dv3!j!&r4hy##gvsrnr)+oqc#3g)1xe&wh%"

GOOGLE_MAPS_API_KEY = "AIzaSyCQ9bqrZcaPrIMRE8T3IgtXNVeocvr5tfk"

DEBUG = True
ALLOWED_HOSTS = ["*"]

DJANGO_SETTINGS_MODULE = "eat_explorer.settings.local"

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "eat_explorer",  # Choose a name for your database
        "USER": "abdullah.nafees",  # Choose a username
        "PASSWORD": "daddy23",  # Choose a password
        "HOST": "localhost",  # Change to your PostgreSQL host if necessary
        "PORT": "5432",  # Use the default PostgreSQL port
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]
