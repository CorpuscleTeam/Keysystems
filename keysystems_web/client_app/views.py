from django.shortcuts import render, redirect
from django.http.request import HttpRequest

from .forms import AuthUserForm
from .models import news, OrderTopic, Soft
from django.core.serializers import serialize
from base_utils import log_error
from enums import RequestMethod


# удалить аналог 2_2
def index_3_2(request: HttpRequest):
    context = {}
    return render(request, 'index_3_2.html', context)


# страничка с новостями
def index_4_1(request: HttpRequest):
    if request.method == RequestMethod.POST:
        log_error(RequestMethod.POST, wt=False)

    topics = OrderTopic.objects.filter(is_active=True).all()
    soft = Soft.objects.filter(is_active=True).all()
    soft_json = serialize('json', soft)
    topics_json = serialize('json', topics)
    context = {
        'news': news,
        'topics': topics_json,
        'soft': soft_json,
        'orders_count': 2,
        'notice': 10,
        'update_count': 20,
    }
    return render(request, 'index_4_1.html', context)


def index_4_2(request: HttpRequest):
    context = {
    }
    return render(request, 'index_4_2.html', context)
