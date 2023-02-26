
import settings_base


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': settings_base.BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = False

ALLOWED_HOSTS = [
    'www.matthewhill.click',
]