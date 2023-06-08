
from pathlib import Path
from json import load
from os import environ


def setup():

    with open(Path(__file__).resolve().parent.parent / "conf" / "portfolio.env") as f:

        env_data = load(f)

        for variable in env_data:

            environ[variable] = env_data[variable]


    if "DJANGO_SETTINGS_MODULE" in environ:
        if environ["DJANGO_SETTINGS_MODULE"][8:] not in ["test", "live"]:
            environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.test')