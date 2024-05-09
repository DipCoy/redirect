FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV POETRY_VERSION=1.2.2
ARG ENV

RUN mkdir -p /src/

RUN apt-get update \
    && pip install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false

COPY pyproject.toml pyproject.toml

RUN poetry install

COPY src/ /src/
WORKDIR /src/
