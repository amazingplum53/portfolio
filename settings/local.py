
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

#/usr/bin/openssl req -x509 -newkey rsa:4096 -keyout $VOLUMEDIR/key.pem -out $VOLUMEDIR/cert.pem -sha256 -days 365 -config $BASEDIR/conf/openssl.cnf -nodes

subprocess.run([
    "/usr/bin/openssl", "req", "-x509", "-newkey", "rsa:4096", 
    "-keyout", f"{VOLUME_DIR}/key.pem",
    "-out", f"{VOLUME_DIR}/cert.pem", 
    "-sha256", "-days", "365", 
    "-config", f"{BASE_DIR}/conf/openssl.cnf", 
    "-nodes"
])              

