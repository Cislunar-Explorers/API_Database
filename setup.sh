#!/bin/bash

python3 -m venv django-venv
source django-venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver