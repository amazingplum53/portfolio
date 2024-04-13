
"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ
from pathlib import Path
from subprocess import run
from sys import path

BASE_DIR = Path(__file__).resolve().parent.parent

path.append(BASE_DIR)

environ["BASE_DIR"] = str(BASE_DIR)

max_workers = cpu_count

bind = '0.0.0.0:' + environ.get('PORT', '8000')

max_requests = 1000

worker_class = 'gevent'

workers = max_workers()


def on_starting(server):

    from portfolio.env import get_environ_variables, generate_env

    run(["/usr/bin/git", "pull"])

    try:

        get_environ_variables(BASE_DIR)

    except:
        generate_env(BASE_DIR)
        get_environ_variables(BASE_DIR)