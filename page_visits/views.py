from django.shortcuts import render
from django.http import HttpResponse
from .models import PageVisits

# Create your views here.
def hello_world(request):
    page_visits = PageVisits.objects.first()
    if not page_visits:
        page_visits = PageVisits.objects.create(count=1)
    else:
        page_visits.count += 1
        page_visits.save()
    return HttpResponse('Hello World! You are visitor no. {0}.'.format(page_visits.count))
