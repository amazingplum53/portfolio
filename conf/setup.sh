#!/usr/bin/bash

BASEDIR="/var/www/portfolio/"

VOLUMEDIR="/data/certificates/portfolio"

cd $BASEDIR

/usr/bin/git pull

/usr/bin/openssl req -x509 -newkey rsa:4096 -keyout $VOLUMEDIR/key.pem -out $VOLUMEDIR/cert.pem -sha256 -days 365 -config $BASEDIR/conf/openssl.cnf -nodes

/usr/sbin/nginx
