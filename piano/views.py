#!/usr/bin/env python
# encoding: utf-8
from django.http import Http404
from django.shortcuts import render_to_response
from piano.models import *
from django.http import HttpResponse

def home_page(request):
    return render_to_response('home.html')


# 注册页面
def sign_up_page(request):
    return render_to_response("sign_up.html")

def sign_up_form(request):
    print('sign_up_form')
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    elif not is_legal_sign_up(request):
        return HttpResponse('注册信息有误，已存在的用户名或者邮箱')
    else:
        user = User()
        user.name = request.POST['username']
        print(user.name)
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.save()
        return render_to_response('home.html')

def is_legal_sign_up(request):
    all_users = User.objects.all()
    for user in all_users:
        if user.name == request.POST['username'] or user.email == request.POST['email']:
            return False
    return True


# 登陆页面
def sign_in_page(request):
    return render_to_response("sign_in.html")

def sign_in_form(request):
    if request.method == 'POST' and is_sign_in_correct(request):
        request.session['is_login'] = True  # session记录登录状态
        request.session['email'] = request.POST['email']
        return render_to_response('home.html')
    else:
        return HttpResponse('登录信息错误')

def is_sign_in_correct(request):
    print(request.POST['email'])
    try:
        user = User.objects.get(email=request.POST['email'])
        print(55, user)
        real_password = user.password
        input_password = request.POST['password']
        print('input password:', input_password)
        return real_password == input_password
    except User.DoesNotExist:
        print('false')
        return False

# 发布钢琴页面
def release_piano_page(request):
    if request.session.get('is_login'):
        return HttpResponse('需要登录')
    else:
        return render_to_response("release_piano.html")

def release_piano_form(request):
    print('release_piano_form')

    if request.method == 'POST' and request.session.get('is_login'):
        save_piano(request)
        return render_to_response('home.html')
    else:
        print("fail to release")
        return HttpResponse("发布信息失败")

def save_piano(request):
    piano = Piano()
    piano.title = request.POST['title']
    piano.info = request.POST['info']
    piano.brand = request.POST['brand']
    print(piano.brand)
    piano.price = request.POST['price']
    piano.use_time = request.POST['use_time']
    piano.image_link = request.POST['image_link']

    piano.seller = User.objects.get(email=request.session.get('email'))
    print(piano.seller)
    piano.save()


# 注销
def cancel(request):
    if request.session.get('is_login'):
        User.objects.filter()
        return HttpResponse('注销成功')
