from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
from models import Point

import logging
# logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    print request.GET
    return HttpResponse("HELLO")

def incoming(request):
    logging.warning(request.GET)
    try:
        # p#, lat, long, timestamp
        message = request.GET['text']
        data = message.split(',')
        p = Point(lat=data[1], long=data[2], time=datetime.fromtimestamp(data[3]))
        p.save()
    except Exception:
        print "Not Recorded"
        pass

    return HttpResponse("RECEIVING SMS")
