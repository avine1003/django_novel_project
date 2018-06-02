# -*- coding: utf-8 -*-
from django.conf.urls import url

__author__ = "wuyou"
__date__ = "2018/5/31 12:05"

from .views import message_submit

urlpatterns = [
   url(r'^$', message_submit, name='go_form'),
]