
from .base import BASE_DIR
from os import environ


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'HOST': environ["server hostname"],
        'USER': environ["server username"],
        'PASSWORD': environ["server password"],
        'PORT': 5432,
    }
}


