
"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ
import subprocess
from portfolio.env import get_environ_variables, generate_env
from settings.base import BASE_DIR
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

    try:
        get_environ_variables(BASE_DIR)

    except:
        generate_env(BASE_DIR)
        get_environ_variables(BASE_DIR)

    if environ["SETTINGS"] in ["test", "live"]:

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
        
