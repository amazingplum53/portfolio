
"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ
from os.path import isdir
import subprocess
from portfolio.env import get_environ_variables, generate_env
from settings.base import BASE_DIR, VOLUME_DIR


max_workers = cpu_count

bind = '0.0.0.0:' + environ.get('PORT', '8000')

max_requests = 1000

worker_class = 'gevent'

workers = max_workers()

preload_app = True


def on_starting(server):

    subprocess.run(["/usr/bin/git", "pull"])

    if isdir("/certificates/portfolio"):

        subprocess.run(["mkdir", '/certificates/portfolio/'])

        try:
            get_environ_variables(BASE_DIR)

        except:
            generate_env(BASE_DIR)
            get_environ_variables(BASE_DIR)

        if environ["SETTINGS"] in ["test", "live"]:
            pass
        else:

            #/usr/bin/openssl req -x509 -newkey rsa:4096 -keyout $VOLUMEDIR/key.pem -out $VOLUMEDIR/cert.pem -sha256 -days 365 -config $BASEDIR/conf/openssl.cnf -nodes

            subprocess.run(
                [
                    "/usr/bin/openssl", "req", "-x509", "-newkey", "rsa:4096", 
                    "-keyout", f"{VOLUME_DIR}/key.pem",
                    "-out", f"{VOLUME_DIR}/cert.pem", 
                    "-sha256", "-days", "365", 
                    "-config", f"{BASE_DIR}/conf/openssl.cnf", 
                    "-nodes"
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT
            )  


def when_ready(server):
    subprocess.run(["/usr/sbin/nginx"])
