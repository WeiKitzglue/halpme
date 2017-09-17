from django.shortcuts import render
from django.http import HttpResponse
from models import Point

import logging
# logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    print request.GET
    return HttpResponse("HELLO")

def incoming(request):
    logging.warning(request.GET)
    message = request.GET['text']
    coord = message.split(',')
    p = Point(lat=coord[0], long=coord[1])
    p.save()

    return HttpResponse("RECEIVING SMS")
