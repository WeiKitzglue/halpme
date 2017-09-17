from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
from models import Point
import requests

import logging
import json

FEATURELAYER_URL = 'https://services8.arcgis.com/j1t3CMZN0P8OmjOH/arcgis/rest/services/halp/FeatureServer/0'

# Create your views here.
def index(request):
    points = Point.objects.all()
    return render(request, 'findme/index.html', {'points': points})


def post(lat, long, time):
    feature = [
        {
            "geometry" : {"x" : lat, "y" : long},
            "attributes" : {
                "id" : 1,
                "time": time
            }
        }
    ]
    logging.info(requests.post('{}/addFeatures'.format(FEATURELAYER_URL),
                               data={
                                   'f': 'json',
                                   'features': json.dumps(feature)
                               }))


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


