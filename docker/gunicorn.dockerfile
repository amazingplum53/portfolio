FROM python:latest

ENV BASEDIR="/var/www" 

WORKDIR $BASEDIR

RUN git clone https://github.com/amazingplum53/portfolio.git portfolio

#COPY portfolio.env portfolio/docker/

RUN python3 -m pip install -r portfolio/docker/gunicorn/requirements.txt

#ENV RUN_COMMAND="gunicorn portfolio.wsgi --chdir $BASEDIR/portfolio/portfolio -c $BASEDIR/portfolio/docker/gunicorn/gunicorn.config.py"

#RUN echo 'alias run="$RUN_COMMAND"' >> ~/.bashrc