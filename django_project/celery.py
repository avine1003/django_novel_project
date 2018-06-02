# -*- coding: utf-8 -*-
from __future__ import absolute_import,unicode_literals
__author__ = "wuyou"
__date__ = "2018/5/31 14:43"

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

# 创建celery应用
app = Celery('django_project')
# You can pass the object directly here, but using a string is better since then the worker doesn’t have to serialize the object.
app.config_from_object('django.conf:settings')
# 如果在工程的应用中创建了tasks.py模块，那么Celery应用就会自动去检索创建的任务。比如你添加了一个任#务，在django中会实时地检索出来。
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
