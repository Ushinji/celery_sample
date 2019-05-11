FROM python:3.7.1 as base

ENV LANG C.UTF-8
ENV APP_ROOT=/app/

RUN apt update -qq \
  && apt install -y build-essential mysql-client --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

WORKDIR /app
COPY Pipfile* $APP_ROOT
RUN pipenv install --dev
