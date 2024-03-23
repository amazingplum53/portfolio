
"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ
from os.path import isdir
import subprocess
from portfolio.env import get_environ_variables, generate_env
from settings.base import BASE_DIR, VOLUME_DIR
import tempfile
import json


max_workers = cpu_count

bind = '0.0.0.0:' + environ.get('PORT', '8000')

max_requests = 1000

worker_class = 'gevent'

workers = max_workers()

preload_app = True

change_config = """
{
    "Comment": "Update IP address",
    "Changes": [
        {
            "Action": "UPSERT",
            "ResourceRecordSet": {
                "Name": "matthewhill.click.",
                "Type": "A",
                "TTL": 300,
                "ResourceRecords": [
                    {
                        "Value": "{ip_address:.2f}"
                    }
                ]
            }
        }
    ]
}
"""


def on_starting(server):

    subprocess.run(["/usr/bin/git", "pull"])

    if not isdir("/certificates/portfolio"):

        try:
            get_environ_variables(BASE_DIR)

        except:
            generate_env(BASE_DIR)
            get_environ_variables(BASE_DIR)
        
        if not isdir("/certificates"):
            subprocess.run(["mkdir", '/certificates'])

        subprocess.run(["mkdir", '/certificates/portfolio/'])

        if environ["SETTINGS"] in ["test", "live"]:

            # Configure AWS CLI

            subprocess.run(["aws", "configure", "set", "aws_access_key_id", environ["aws_access_key_id"]])
            subprocess.run(["aws", "configure", "set", "aws_secret_access_key", environ["aws_secret_access_key"]])
            subprocess.run(["aws", "configure", "set", "default.region", "eu-west-2"])
            
            # Get public IP

            public_ip = subprocess.run( 
                ["dig", "+short", "myip.opendns.com", "@resolver1.opendns.com"],
                capture_output = True,
                text = True
            )

            change_config = change_config.format(ip_address = public_ip)

            # Create config file
            
            with tempfile.TemporaryDirectory() as temp_dir:

                with open(temp_dir.name / 'change-config.json', 'w') as f:
                    json.dump(change_config, f)

                # Change hostname to current IP address

                subprocess.run(["aws", "route53", "change-resource-record-sets", "--hosted-zone-id", "Z026733134QMX0B8C9RSV", "--change-batch", f"{temp_dir.name}/change-config.json"])

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
