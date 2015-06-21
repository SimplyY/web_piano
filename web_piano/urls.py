"""web_piano URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import *
from django.contrib import admin
from piano.views import *
from piano import views

# 模式包含了一个尖号(^)和一个美元符号($)。这些都是正则表达式符号，并且有特定的含义：
# 上箭头要求表达式对字符串的头部进行匹配，美元符号则要求表达式对字符串的尾部进行匹配。
urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),
                       ('home$', home_page),
                       ('sign_up$', sign_up_page),
                       ('sign_up_form$', sign_up_form),
                       ('sign_in$', sign_in_page),
                       ('sign_in_form$', sign_in_form),
                       ('release_piano$', release_piano_page),
                       ('release_piano_form$', release_piano_form),
                       ('exit', views.exit),
                       ('cancel', cancel),

)
