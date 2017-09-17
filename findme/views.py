from django.shortcuts import render
from django.http import HttpResponse
import logging
# logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    print request.GET
    return HttpResponse("HELLO")

def incoming(request):
    logging.warning(request.GET)
    return HttpResponse("SMS")
