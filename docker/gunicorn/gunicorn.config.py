
"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ
from portfolio.env import get_environ_variables, generate_env
from settings.base import BASE_DIR
from subprocess import run

max_workers = cpu_count

bind = '0.0.0.0:' + environ.get('PORT', '8000')

max_requests = 1000

worker_class = 'gevent'

workers = max_workers()


def on_starting(server):

    run(["/usr/bin/git", "pull"])

    try:
        get_environ_variables(BASE_DIR)

    except:
        generate_env(BASE_DIR)
        get_environ_variables(BASE_DIR)