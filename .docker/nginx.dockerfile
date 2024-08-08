FROM nginx:latest

WORKDIR /etc/nginx/

COPY nginx/http.conf /etc/nginx/

RUN mkdir /static/

COPY ../static /static/

EXPOSE 80

ENTRYPOINT ["bash", "-c"]

CMD ["nginx -c /etc/nginx/http.conf -g 'daemon off;'"]
