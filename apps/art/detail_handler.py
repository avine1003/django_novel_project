# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render

from art.models import Art
from django_project.settings import logger

__author__ = "wuyou"
__date__ = "2018/5/30 10:50"


def detail_handler(request):
    logger.info("detailHandler request Handler begin")
    # id = self.get_argument("id", None)
    id = request.GET.get("id", None)
    if id == None:
        return HttpResponseRedirect("/art/index")
    else:
        art = Art.objects.get(id=int(id))
        context = {"art": art}
        return render(request, "home/detail.html", context=context)
