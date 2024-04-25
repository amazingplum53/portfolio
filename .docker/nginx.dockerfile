FROM nginx:latest

WORKDIR /etc/nginx/

COPY nginx/nginx.conf /etc/nginx/nginx.conf

COPY nginx/controller.sh /var/

RUN chmod +x /var/controller.sh
