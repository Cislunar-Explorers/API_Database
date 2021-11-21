# About
This program contains a Django API connected to an embedded SQLite database. API endpoints follow Django REST and Grafana query conventions. 

# Set Up Instructions
1. Environment: create a virtual environment, cd into virtual environment, and install requirements.
```
python -m venv venv
cd venv
pip install -r requirements
```
2. Database: create and migrate sqlite table
```
python manage.py makemigrations
python manage.py migrate
```
3. Django API: Run the server!
```
python manage.py runserver
```
