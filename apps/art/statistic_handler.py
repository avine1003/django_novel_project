# -*- coding: utf-8 -*-
from django.shortcuts import render

__author__ = "wuyou"
__date__ = "2018/6/2 10:29"


def histogram_handler(request):
   import json
   myjson = {
      'type': 'column',
      'colorByPoint': 'true',
      'data': [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
      'showInLegend': 'true'
   }
   data = json.dumps(myjson)
   return render(request, "statics/art_statics.html", locals())
