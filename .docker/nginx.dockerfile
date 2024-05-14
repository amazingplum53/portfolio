FROM nginx:latest

WORKDIR /etc/nginx/

COPY nginx/http.conf /etc/nginx/
COPY nginx/https.conf /etc/nginx/

