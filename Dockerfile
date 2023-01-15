FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN mkdir /api

WORKDIR /api

COPY pyproject.toml pyproject.toml

ADD pyproject.toml /api/

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

ADD . /api/
