#--------- Generic stuff all our Dockerfiles should start with so we get caching ------------
# Note this base image is based on debian
# Tim Sutton, December 2014

FROM python:2.7
MAINTAINER Alison Mukoma<alison@kartoza.com>

RUN  export DEBIAN_FRONTEND=noninteractive
ENV  DEBIAN_FRONTEND noninteractive
RUN  dpkg-divert --local --rename --add /sbin/initctl

# Use local cached debs from host (saves your bandwidth!)
# Change ip below to that of your apt-cacher-ng host
# Or comment this line out if you do not with to use caching
ADD 71-apt-cacher-ng /etc/apt/apt.conf.d/71-apt-cacher-ng
RUN apt-get -y update
RUN apt-get -y install \
    python-gdal \
    npm \
    nodejs \
    rpl
RUN npm -g install yuglify

# Debian is messed up and aliases node as nodejs
# So when yuglify is installed it references the wrong node binary...
# lets fix that here...

RUN rpl "env node" "env nodejs" /usr/local/lib/node_modules/yuglify/bin/yuglify

RUN apt-get install locales && \
    echo "en_ZA.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_ZA.UTF-8
ENV LANG en_ZA.UTF-8
ENV LANGUAGE en_ZA:en
ENV LC_ALL en_ZA.UTF-8

ADD REQUIREMENTS.txt /REQUIREMENTS.txt
RUN pip install -r /REQUIREMENTS.txt

RUN apt-get update -y; apt-get -y --force-yes install yui-compressor

# Install translation
RUN apt-get -y --force-yes install gettext

# Open port 8080 as we will be running our uwsgi socket on that
EXPOSE 8080

WORKDIR /home/web/django_project

# Using daphne server for running channel.
CMD ["daphne", "-b", "0.0.0.0", "-p", "8080", "core.asgi:channel_layer"]