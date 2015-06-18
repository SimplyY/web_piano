#!/usr/bin/env python
# encoding: utf-8
from django.shortcuts import render_to_response
import datetime
from django.template import Template

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response("current_datatime.html", {'current_date': now})
