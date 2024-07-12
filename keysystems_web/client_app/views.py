from django.shortcuts import render, redirect
from django.http.request import HttpRequest

from .forms import AuthUserForm
from .models import news, OrderTopic, Soft
from base_utils import log_error
from enums import RequestMethod


# удалить аналог 2_2
def index_3_2(request: HttpRequest):
    context = {}
    return render(request, 'index_3_2.html', context)


# страничка с новостями
def index_4_1(request: HttpRequest):
    if request.method == RequestMethod.POST:
        pass

    topics = OrderTopic.objects.filter(is_active=True).all()
    soft = Soft.objects.filter(is_active=True).all()
    context = {
        'news': news,
        'topics': topics,
        'soft': soft,
    }
    return render(request, 'index_4_1.html', context)


def index_4_2(request: HttpRequest):
    context = {
    }
    return render(request, 'index_4_2.html', context)
