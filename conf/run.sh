#!/usr/bin/bash

cd /var/www/portfolio/

/usr/bin/git pull

/usr/bin/supervisorctl start supervisor

echo "Hello world"

while :; do sleep 2073600; done