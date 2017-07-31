FROM python:3.6.1
MAINTAINER Fred Chevitarese <fchevitarese@gmail.com>

ENV PYTHONBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD . /code/
RUN mv .env.initial .env && pip install -r requirements.txt
