import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# def index(request):
#     return render(request, 'index.html')

def add_handler(request):
    x = request.GET.get('x', '1')
    y = request.GET.get('y', '1')
    from .tasks import add
    add.delay(int(x), int(y))
    res = {'code': 200, 'message': 'ok', 'data': {'x': x, 'y': y}}
    return HttpResponse(json.dumps(res))


def render_index(request):
    return render(request, "statics/index.html")

