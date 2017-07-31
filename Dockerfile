FROM python:3.6.1
MAINTAINER Fred Chevitarese <fchevitarese@gmail.com>

ENV PYTHONBUFFERED 1

RUN mkdir /code
WORKDIR /code
RUN mkdir media && mkdir CACHE

ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/
