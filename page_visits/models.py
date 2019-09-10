from django.db import models

# Create your models here.

class PageVisits(models.Model):
    count = models.IntegerField()

class ScheduledTaskRunCount(models.Model):
    count = models.IntegerField()
