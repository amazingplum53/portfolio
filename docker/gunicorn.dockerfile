FROM python:latest

ENV BASEDIR="/var/www" 

RUN git clone https://github.com/amazingplum53/portfolio.git $BASEDIR/portfolio

WORKDIR $BASEDIR/portfolio

RUN cp docker/gunicorn/gunicorn.config.py ./

RUN python3 -m pip install -r docker/gunicorn/requirements.txt
