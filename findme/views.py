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
            "geometry" : {"x" : long, "y" : lat},
            "attributes" : {
                "id" : 1,
                "time": int(time)
            }
        }
    ]
    response = requests.post('{}/addFeatures'.format(FEATURELAYER_URL),
                               data={
                                   'f': 'json',
                                   'features': json.dumps(feature)
                               })

    logging.info(response.text)


def incoming(request):
    logging.warning(request.GET)
    try:
        # p#, lat, long, timestamp
        message = request.GET['text']
        phone_no, lat, long, time = message.split(',')
        p = Point(phone_no=phone_no, lat=lat, long=long, time=datetime.fromtimestamp(time))
        p.save()
    except Exception:
        print "Not Recorded"
        pass

    return HttpResponse("RECEIVING SMS")


