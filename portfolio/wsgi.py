"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""


from django.core.wsgi import get_wsgi_application

from .get_env import setup

setup()

application = get_wsgi_application()
