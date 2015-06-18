#!/usr/bin/env python
# encoding: utf-8
from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response("sign_in.html", {'current_date': now})
