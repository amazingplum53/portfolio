
"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ
import subprocess


max_workers = cpu_count

bind = '0.0.0.0:' + environ.get('PORT', '8000')

max_requests = 1000

worker_class = 'gevent'

workers = max_workers()

def when_ready(server):
    subprocess.run(["bash", "/var/www/conf/setup.sh"])
