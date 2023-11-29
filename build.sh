#!/usr/bin/env bash
# exit on errorbggy
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate


git config --global user.name "sowDragnir"
git config --global user.email neybassj@gmail.com