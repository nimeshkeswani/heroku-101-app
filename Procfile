release: python manage.py migrate
web: gunicorn heroku_101_app.wsgi --log-file -
worker: celery worker --app=heroku_101_app.celery --loglevel=INFO
beat: celery beat --app=heroku_101_app.celery --loglevel=INFO
