#!/usr/bin/env sh

# exit on error
set -o errexit

poetry install

poetry run ./manage.py collectstatic --no-input
poetry run ./manage.py migrate


