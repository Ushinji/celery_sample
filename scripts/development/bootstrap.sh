#!/bin/sh

set -e

echo "### Development environment bootstrap ###"
echo ""

docker-compose build
docker-compose run --rm app pipenv install --dev
docker-compose run --rm app pipenv run python migrations/create_database.py
docker-compose run --rm app pipenv run db_upgrade
docker-compose up -d
