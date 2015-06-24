#!/usr/bin/env python
# encoding: utf-8
from django.http import Http404
from django.shortcuts import render_to_response
from piano.models import *
from django.template import Context
from django.http import HttpResponse

return_to_home = "<a href='home'>点击回到首页</a>"

def response_home_page(request):
    return render_to_response('home.html', Context({'is_sign_in': request.session.get('is_sign_in'),
                                                    'pianos': Piano.objects.all()}))
def response_piano_page(piano):
    return render_to_response('piano.html', Context({'piano': piano, 'comments': Comment.objects.all()}))

def home_page(request):
    return response_home_page(request)


# 注册页面
def sign_up_page(request):
    return render_to_response("sign_up.html")
# 响应注册表单
def sign_up_form(request):
    print('sign_up_form')
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    elif not is_legal_sign_up(request):
        return HttpResponse('注册信息有误，已存在的用户名或者邮箱' + return_to_home)
    else:
        user = User()
        user.name = request.POST['username']
        print(user.name)
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.save()
        return response_home_page(request)

def is_legal_sign_up(request):
    all_users = User.objects.all()
    for user in all_users:
        if user.name == request.POST['username'] or user.email == request.POST['email']:
            return False
    return True


# 登陆页面
def sign_in_page(request):
    return render_to_response("sign_in.html")
# 响应登陆表单
def sign_in_form(request):
    if request.method == 'POST' and is_sign_in_correct(request):
        request.session['is_sign_in'] = True  # session记录登录状态
        request.session['email'] = request.POST['email']
        print(request.session.get('is_sign_in'))
        return response_home_page(request)
    else:
        return HttpResponse('登录信息错误' + return_to_home)

def is_sign_in_correct(request):
    print(request.POST['email'])
    try:
        user = User.objects.get(email=request.POST['email'])
        real_password = user.password
        input_password = request.POST['password']
        return real_password == input_password
    except User.DoesNotExist:
        return False

# 发布钢琴页面
def release_piano_page(request):
    if request.session.get('is_sign_in'):
        return render_to_response("release_piano.html")
    else:
        return HttpResponse('需要登录' + return_to_home)
# 响应发布钢琴的表单
def release_piano_form(request):
    print('release_piano_form')

    if request.method == 'POST' and request.session.get('is_sign_in'):
        save_piano(request)
        return response_home_page(request)
    else:
        print("fail to release")
        return HttpResponse("发布信息失败" + return_to_home)
# 将新发布的piano写入数据库
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

# 单个钢琴页面
def piano_page(request):
    url = request.get_full_path()
    for piano in Piano.objects.all():
        print(str(piano.id))
        print(url[6::])
        if str(piano.id) == url[6::]:
            request.session['current_piano_id'] = piano.id
            return response_piano_page(piano)
    return HttpResponse('点击未找到相应钢琴')

# 处理单个钢琴页面的评论表单
def comment_form(request):
    if request.session.get('is_sign_in'):
        if request.method == 'POST':
            user = User.objects.get(email=request.session.get('email'))
            comment_content = request.POST['comment']
            piano_id = request.session.get('current_piano_id')
            piano = Piano.objects.get(id=piano_id)
            comment = Comment()
            comment.content = comment_content
            comment.piano = piano
            comment.user = user
            comment.save()
            return HttpResponse('评论成功，' + return_to_home)
    else:
        return HttpResponse('未登录无法评论，请先登录。' + return_to_home)


# 修改密码
def change_password_page(request):
    return render_to_response('change_password.html')

def change_password_form(request):
    fail_change = '更改密码失败,'
    incorrect_password = '密码错误,'
    if request.method == 'POST' and request.session.get('is_sign_in'):
        user = User.objects.get(email=request.session.get('email'))
        print(user)
        if request.POST['oldpassword'] == user.password:
            user.password = request.POST['newpassword']
            user.save()
            return response_home_page(request)
        else:
            return HttpResponse(incorrect_password + return_to_home)
    else:
        return HttpResponse(fail_change + return_to_home)


# 注销
def cancel(request):
    if request.session.get('is_sign_in'):
        user = User.objects.get(email=request.session.get('email'))
        user.delete()
        delete_sign_in_session(request)
        return HttpResponse("注销成功," + return_to_home)
    else:
        return HttpResponse("注销失败," + return_to_home)

def exit(request):
    if request.session.get('is_sign_in'):
        delete_sign_in_session(request)
        return HttpResponse("退出成功," + return_to_home)
    else:
        return HttpResponse("退出失败," + return_to_home)
# 将session里关于sign_in的内容置空
def delete_sign_in_session(request):
    request.session['is_sign_in'] = False
    request.session['email'] = None
