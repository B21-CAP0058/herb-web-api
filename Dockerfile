FROM python:3.6.13-slim-buster
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=main.py
# install dependencies
RUN apt-get update && apt-get install -y  default-libmysqlclient-dev gcc g++ build-essential 
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
# copy project
COPY . /usr/src/app/
CMD ["flask","run","--host=0.0.0.0"]
