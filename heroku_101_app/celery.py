from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'heroku_101_app.settings')
app = Celery('heroku_101_app')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Schedule
app.conf.beat_schedule = {
    'every-10-seconds': {  #name of the scheduler
        'task': 'increment_scheduled_task_run_count',  # task name which we have created in tasks.py
        'schedule': 10.0,   # set the period of running
        'args': None  # set the args
    },
}

@app.task(bind=True)
def debug_task(self):
    print('Test Request: {0!r}'.format(self.request))