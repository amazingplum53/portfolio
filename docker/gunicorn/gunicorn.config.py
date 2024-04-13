
"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ
from subprocess import run
from sys import path

max_workers = cpu_count

bind = '0.0.0.0:' + environ.get('PORT', '8000')

max_requests = 1000

worker_class = 'gevent'

workers = max_workers()

path.append("/var/www/portfolio")


def on_starting(server):

    from portfolio.env import get_environ_variables, generate_env

    run(["/usr/bin/git", "pull"])

    try:

        get_environ_variables()

    except:
        generate_env()
        get_environ_variables()