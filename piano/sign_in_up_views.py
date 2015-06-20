#!/usr/bin/env python
# encoding: utf-8
from django.shortcuts import render_to_response
from piano.models import *


def sign_up_page(request):
    return render_to_response("sign_up.html")


def sign_up_form(request):
    print('sign_up_form')

    if request.method == 'GET':
        user = User()
        user.name = request.GET['username']
        print(user.name)
        user.email = request.GET['email']
        user.password = request.GET['password']
        user.save()
        return render_to_response('home.html')
    else:
        return render_to_response('wrong.htm')


def sign_in_page(request):
    return render_to_response("sign_in.html")


def sign_in_form(request):
    if request.method == 'POST' and is_sign_in_correct(request):
        save_login_status()
        return render_to_response('home.html')
    else:
        return render_to_response('wrong url')



def is_sign_in_correct(request):
    user = User.objects.filter(email=request['email'])
    real_password = user['password']
    input_password = request['password']
    print('real password:', real_password)
    print('input password:', input_password)
    return real_password == input_password


def save_login_status():
    # TODO
    pass
