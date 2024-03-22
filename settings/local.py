
from .base import BASE_DIR, VOLUME_DIR
import subprocess


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]            

