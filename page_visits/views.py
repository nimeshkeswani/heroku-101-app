from django.shortcuts import render
from django.http import HttpResponse
from .models import PageVisits
from .tasks import increment_page_visit
from heroku_101_app.celery import debug_task
import logging
import datetime


logger = logging.getLogger(__name__)


# Create your views here.
def hello_world(request):
    page_visits = PageVisits.objects.first()
    if not page_visits:
        page_visits = PageVisits.objects.create(count=1)
    else:
        increment_page_visit.delay()
    logger.info('New Visitor on {0}'.format(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
    return HttpResponse('Hello World! You are visitor no. {0}.'.format(page_visits.count + 1))
