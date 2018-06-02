# -*- coding: utf-8 -*-
__author__ = "wuyou"
__date__ = "2018/5/31 14:44"

import time
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from django_project.celery import app

# @app.task
# def tsend_email():
#    url = "http://1000phone.com"
#    receiver = 'zhouguangyou@1000phone.com'
#    content = pack_html(receiver, url)
#    # content = 'this is email content.'
#    send_email(receiver, content)
#    print('send email ok!')
@app.task
def add(x, y):
   return x + y