FROM python:3.6-jessie
ENV PYTHONUNBUFFERED 1
ENV DJANGO_READ_DOT_ENV_FILE 1
ENV DJANGO_SETTINGS_MODULE app.settings

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app

RUN apt-get update
RUN apt-get -y install python3-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary
