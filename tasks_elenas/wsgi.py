"""
WSGI config for tasks_elenas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from decouple import config
from django.core.wsgi import get_wsgi_application

settings_file = config("SETTINGS", cast=str)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", f"tasks_elenas.settings.{settings_file}"
)

application = get_wsgi_application()
