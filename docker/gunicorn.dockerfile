FROM python:latest

ENV BASEDIR="/var/www" 

RUN git clone https://github.com/amazingplum53/portfolio.git $BASEDIR/portfolio

WORKDIR $BASEDIR/portfolio

#COPY portfolio.env portfolio/docker/

COPY docker/gunicorn.dockerfile ./

RUN python3 -m pip install -r docker/gunicorn/requirements.txt

#ENV RUN_COMMAND="gunicorn portfolio.wsgi --chdir $BASEDIR/portfolio/portfolio -c $BASEDIR/portfolio/docker/gunicorn/gunicorn.config.py"

#RUN echo 'alias run="$RUN_COMMAND"' >> ~/.bashrc