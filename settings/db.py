
from .base import BASE_DIR
from os import environ


DATABASE_ROUTERS = [
    'blog.router.BlogRouter', 
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'blog': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'HOST': environ["server hostname"],
        'USER': environ["server username"],
        'PASSWORD': environ["server password"],
        'PORT': 5432,
    }
}


