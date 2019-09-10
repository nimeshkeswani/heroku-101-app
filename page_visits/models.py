from django.db import models

# Create your models here.

class PageVisits(models.Model):
    count = models.IntegerField()
