FROM python:3.7.1 as base

ENV LANG C.UTF-8
ENV APP_ROOT=/app/

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
      build-essential \
      mysql-client \
  && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip \
  && pip install pipenv

RUN mkdir $APP_ROOT
WORKDIR $APP_ROOT
