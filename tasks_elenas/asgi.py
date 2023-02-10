"""
ASGI config for tasks_elenas project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from decouple import config
from django.core.asgi import get_asgi_application

settings_file = config("SETTINGS", cast=str)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", f"tasks_elenas.settings.{settings_file}"
)

application = get_asgi_application()
