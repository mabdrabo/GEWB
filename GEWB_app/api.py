from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.utils import simplejson
from collections import OrderedDict
from GEWB_app.models import *
from GEWB_app.views import *


def add_emergency(request, em_type):
    logged_user = logged_in_user(request)
    if isinstance(logged_user, User):
        try:
            if 'lon' in request.GET and 'lat' in request.GET:
                emergency = Emergency.objects.create(user=logged_user, category=em_type, lon=request.GET['lon'], lat=request.GET['lat'])
                return HttpResponse('DONE ' + str(emergency.pk))
        except Exception, e:
            return e
