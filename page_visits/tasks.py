from heroku_101_app.celery import app
from .models import PageVisits
import logging

logger = logging.getLogger(__name__)


@app.task(bind=True)
def increment_page_visit(self):
    logger.info('Incrementing Page Visits...')
    page_visits = PageVisits.objects.first()
    page_visits.count += 1
    page_visits.save()