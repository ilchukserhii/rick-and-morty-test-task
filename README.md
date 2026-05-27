# rick-and-morty-test-task


## How tu run:
- Create venv: `python -m venv .venv`
- Activate: `source .venv/bin/acticate`
- Install requirements: `pip install -r requirements.txt`
- Create Postgres DB & User
- Copy .evn.sample -> .env and populate with all required data
- Run migrations: `python manage.py migrate`
- Run Redis Server: `docker run -d -p 6379:6379 redis`
- Run celery worker for task handling: `celery -A rick_and_morty_api worker -l INFO`
- Run celery beat for task scheduling: `celery -A rick_and_morty_api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`
- Create schedule for running sync in DB
- Run app: `python manage.py runserver`