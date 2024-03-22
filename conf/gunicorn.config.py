
"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ
import subprocess
from portfolio.env import get_environ_variables, generate


max_workers = cpu_count

bind = '0.0.0.0:' + environ.get('PORT', '8000')

max_requests = 1000

worker_class = 'gevent'

workers = max_workers()

preload_app = True


def on_starting(server):

    subprocess.run(["/usr/bin/git", "pull"])

    try:
        get_environ_variables(".")

    except:
        generate(".")
        get_environ_variables(".")


def when_ready(server):
    subprocess.run(["/usr/sbin/nginx"])
