#!/bin/bash


state=$(< /etc/letsencrypt/state.txt)

current_time=$(date +'%D %T')

if [[ $state == "temp" ]]; then

    dry_run=$(certbot certonly -n -d matthewhill.click -w /var/www/certbot --webroot --email matthewpaulh@hotmail.co.uk --agree-tos --preferred-challenges http-01 --dry-run)

    if [[ "$dry_run" == *"successful"* ]]; then

        rm -rf /etc/letsencrypt/live/matthewhill.click/

        certbot certonly -n -d matthewhill.click -w /var/www/certbot --webroot --email matthewpaulh@hotmail.co.uk --agree-tos --preferred-challenges http-01

        echo "${current_time}" > /etc/letsencrypt/state.txt;

    else

        echo "$dry_run"

    fi

elif [[ $(python3 /var/compare.py "${state}" "${current_time}") == True ]]; then

    certbot renew;

else

    echo "Certificate OK";

fi

while : 
do 
    sleep 24h & wait;
    certbot renew;
    timestamp=$(date +"%D %T"); 
    echo "$timestamp" > /etc/letsencrypt/state.txt 
done

