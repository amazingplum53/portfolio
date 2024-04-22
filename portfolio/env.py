
from json import load
from os import environ
from django.core.management.utils import get_random_secret_key
from pathlib import Path


"""{
    "SECRET_KEY": "abc123",
    "SETTINGS": "local",
    "email application key": "def456",
    "email secret key": "ghi789",
    "server hostname": "somewhere.com",
    "server username": "master",
    "server password": "password"
}"""


BASE_DIR = Path(__file__).resolve().parent.parent


def get_environ_variables():

    with open("/run/secrets/secret_file") as f:

        env_data = load(f)

        for variable in env_data:

            environ[variable] = env_data[variable]


def generate_env():

    with open("/run/secrets/secret_file") as f:

        f.write("{")
        f.write(f"""            
    "SECRET_KEY": "{get_random_secret_key()}",
    "SETTINGS": "local"\n""")
        f.write("}")
