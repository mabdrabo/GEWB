from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.utils import simplejson
from collections import OrderedDict
from GEWB_app.models import *

# Create your views here.

def master(request):
    return render_to_response('master.html', {}, RequestContext(request))


def signup(request):
    if request.POST:
        if 'username' in request.POST and 'wb_id' in request.POST and 'name' in request.POST:
            user, new_object = User.objects.get_or_create(username=request.POST['username'], wb_id=request.POST['wb_id'])
            user.name = request.POST['name']
            user.save()
            request.session['username'] = user.username
            return dashboard(request, dic={'success': "successfuly signed up and logged in as " + user.name})
    return render_to_response('master.html', {'error': 'enter your username'}, RequestContext(request))


def signin(request):
    if request.POST:
        if 'username' in request.POST and 'wb_id' in request.POST:
            try:
                user = User.objects.get(username=request.POST['username'], wb_id=request.POST['wb_id'])
                request.session['username'] = user.username
                return dashboard(request, dic={'success': "logged in as " + user.name})
            except User.DoesNotExist:
                return render_to_response('master.html', {'error': 'user not found'}, RequestContext(request))
    return render_to_response('master.html', {'error': 'enter your username'}, RequestContext(request))


def signout(request):
    if 'username' in request.session:
        del request.session['username']
        return render_to_response('master.html', {'info': "You've Logged out"}, RequestContext(request))
    return render_to_response('master.html', {'info': "You've Logged out"}, RequestContext(request))


def dashboard(request, dic={}):
    if 'username' in request.session:
        try:
            user = User.objects.get(username=request.session['username'])
            follows = user.get_follows()
            return render_to_response('dashboard.html', {'user':user, 'follows':follows}, RequestContext(request))
        except User.DoesNotExist:
            return render_to_response('master.html', {'error': 'please login'}, RequestContext(request))
    return render_to_response('master.html', {'error': 'please login'}, RequestContext(request))


def logged_in_user(request):
    if 'username' in request.session:
        try:
            return User.objects.get(username=request.session['username'])
        except User.DoesNotExist:
            return signin(request)
    return signin(request)
