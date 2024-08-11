
"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ
from subprocess import run
from sys import path
from json import load
from portfolio.env import generate_env

max_workers = cpu_count

bind = '0.0.0.0:' + environ.get('PORT', '8001')

max_requests = 1000

workers = max_workers()

path.append("/var/www/portfolio")

environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')

preload_app = False


def on_starting(server):

    run(["/usr/bin/git", "pull"])    

    if "SETTINGS" not in environ:

        try:
            with open('/var/secrets/environ/env-file', 'r') as f:
                env_data = load(f)

            for key, value in env_data.items():

                environ[key] = value

            print(f"Environment variables loaded. Using {environ['SETTINGS']} settings")            
        
        except:

            generate_env()

            print("Environment variables not found. Using local settings.")

    run(["python3", "manage.py", "migrate"])
