from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
from models import Point
import requests

import logging
import json

FEATURELAYER_URL = 'https://services8.arcgis.com/j1t3CMZN0P8OmjOH/arcgis/rest/services/halp2/FeatureServer/0'

def index(request):
    points = Point.objects.all()
    return render(request, 'findme/index.html', {'points': points})

def demo(request):
    points = Point.objects.all()
    return render(request, 'findme/demo.html', {'points': points})


def post(phone_no, lat, lon, time):
    feature = [
        {
            "geometry" : {"x" : lon, "y" : lat},
            "attributes" : {
                "id" : phone_no,
                "time": int(time)*1000
            }
        }
    ]
    response = requests.post('{}/addFeatures'.format(FEATURELAYER_URL),
                               data={
                                   'f': 'json',
                                   'features': json.dumps(feature)
                               })

    logging.warning(response.text)


def incoming(request):
    logging.warning(request.GET)
    try:
        # p#, lat, long, timestamp
        message = request.GET['text']
        phone_no, lat, lon, time = message.split(',')
        p = Point(phone_no=phone_no, lat=float(lat), lon=float(lon), time=datetime.fromtimestamp(float(time)))
        p.save()
	post(phone_no, lat, lon, time)
    except ValueError as err:
        print "Not Recorded: {}".format(err.args[0])
        raise(err)

    return HttpResponse("RECEIVING SMS")


