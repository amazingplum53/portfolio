
from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = False

ALLOWED_HOSTS = [
    'matthewhill.click',
]

CSRF_TRUSTED_ORIGINS = [ 
    f"http://{address}" for address in ALLOWED_HOSTS
] + [
    f"http://www.{address}" for address in ALLOWED_HOSTS
]
