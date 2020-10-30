FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV TZ=Europe/Moscow

RUN apt-get update -y && apt-get upgrade -y

COPY requrements.txt /{{cookiecutter.project_slug}}/requrements.txt

RUN pip install -r /{{cookiecutter.project_slug}}/requrements.txt
