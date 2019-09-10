from heroku_101_app.celery import app
from .models import PageVisits, ScheduledTaskRunCount
from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@app.task(bind=True)
def increment_page_visit(self):
    logger.info('Incrementing Page Visits...')
    page_visits = PageVisits.objects.first()
    page_visits.count += 1
    page_visits.save()

@shared_task(name = "increment_scheduled_task_run_count")
def increment_scheduled_task_run_count(*args, **kwargs):
    logger.info('Incrementing Scheduled Task Run Count...')
    scheduled_task_run_count = ScheduledTaskRunCount.objects.first()
    if not scheduled_task_run_count:
        scheduled_task_run_count = ScheduledTaskRunCount.objects.create(count=1)
    else:
        scheduled_task_run_count.count += 1
        scheduled_task_run_count.save()
