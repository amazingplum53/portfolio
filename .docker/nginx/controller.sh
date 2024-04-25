#!/bin/bash


while [[ $(< /letsencrypt/state.txt) == "temp" ]]; 
do 
    sleep 1 && echo "..."; 
done 

/usr/sbin/nginx -s reload 

echo "Certbot certificate recieved" 

while :; 
do 
    sleep 12h & wait; 
    /usr/sbin/nginx -s reload; 
done