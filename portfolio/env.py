
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


def get_environ_variables(base_dir):

    with open(base_dir + "/docker/portfolio.env") as f:

        env_data = load(f)

        for variable in env_data:

            environ[variable] = env_data[variable]


def generate_env(base_dir):

    with open(base_dir + "/docker/portfolio.env", "w") as f:

        f.write("{")
        f.write(f"""            
    "SECRET_KEY": "{get_random_secret_key()}",
    "SETTINGS": "local"\n""")
        f.write("}")
