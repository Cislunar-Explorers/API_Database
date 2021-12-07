# Set Up 

1. Clone repository
2. Navigate to cloned root, create virtual environment and install required packages.
```
python3 -m venv django-venv
pip install -r requirements.txt
```
3. Activate venv
```
source django-venv/bin/activate
```
3. Migrate databases
```
python3 manage.py makemigrations
python3 manage.py migrate
```
4. Runserver
```
python3 manage.py runserver
```

# Run Locally
Steps 3 and 4 from above.