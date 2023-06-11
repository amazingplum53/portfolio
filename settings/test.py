
from .base import *
from .db import *

DEBUG = True

ALLOWED_HOSTS = [
    'matthewhill.click',
]

CSRF_TRUSTED_ORIGINS = [ 
    f"https://{address}" for address in ALLOWED_HOSTS
]

