release: python manage.py migrate
web: gunicorn heroku_101_app.wsgi --log-file -
worker: celery worker --app=tasks.app
