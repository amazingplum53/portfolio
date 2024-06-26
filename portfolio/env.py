
from json import load
from os import environ
from django.core.management.utils import get_random_secret_key


"""{
    "SECRET_KEY": "abc123",
    "SETTINGS": "local",
    "email application key": "def456",
    "email secret key": "ghi789",
    "server hostname": "somewhere.com",
    "server username": "master",
    "server password": "password"
}"""


def get_environ_variables():

    with open("/run/secrets/portfolio.env") as f:

        env_data = load(f)

        for variable in env_data:

            environ[variable] = env_data[variable]


def generate_env():

    # If settings aren't found generate generate values

    environ["SECRET_KEY"] = get_random_secret_key()
    environ["SETTINGS"] = "local"
