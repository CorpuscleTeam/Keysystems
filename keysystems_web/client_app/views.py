from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize
from datetime import datetime

import os
import json

from keysystems_web.settings import FILE_STORAGE
from .forms import OrderForm
from .models import News
from . import client_utils as utils
from common.models import OrderTopic, Soft, Order, DownloadedFile
from common import log_error, months_str_ru
from enums import RequestMethod


# удалить аналог 2_2
def index_3_2(request: HttpRequest):
    context = {}
    return render(request, 'index_3_2.html', context)

'''
'type_appeal': ['1'], 
'type_soft': ['1'], 
'description': ['уаккав'], 
'addfile': ['Снимок экрана 2024-05-25 162508.png']}>
'''


# страничка с новостями
def index_4_1(request: HttpRequest):
    if request.method == RequestMethod.POST:
        log_error(request.POST, wt=False)
        order_form = OrderForm(request.POST, request.FILES)
        log_error(f'>>>> {order_form.is_valid()}', wt=False)
        if order_form.is_valid():
            utils.order_form_processing(request=request, form=order_form)
            return redirect('redirect')

    news = News.objects.filter(is_active=True).all()
    news_json = serialize(format='json', queryset=news)

    news_data = json.loads(news_json)

    for item in news_data:
        created_at = item['fields']['created_at']
        created_at_date = datetime.fromisoformat(created_at)  # Преобразуем строку в объект datetime
        item['fields']['day'] = created_at_date.day
        item['fields']['month'] = months_str_ru.get(created_at_date.month, '')
        item['fields']['year'] = created_at_date.year

    news_json = json.dumps(news_data)  # Преобразуем обратно в JSON

    client_data = utils.get_main_client_front_data(request)
    context = {
        **client_data,
        'news': news_json,
    }
    return render(request, 'index_4_1.html', context)


def index_4_2(request: HttpRequest):
    client_data = utils.get_main_client_front_data(request)
    context = {
        **client_data,
    }
    return render(request, 'index_4_2.html', context)


def index_8(request: HttpRequest):
    client_data = utils.get_main_client_front_data(request)
    context = {
        **client_data,
    }
    return render(request, 'index_8.html', context)


def index_5_1(request: HttpRequest):
    client_data = utils.get_main_client_front_data(request)
    context = {
        **client_data,
    }
    return render(request, 'index_5_1.html', context)


def index_6(request: HttpRequest):
    client_data = utils.get_main_client_front_data(request)
    context = {
        **client_data,
    }
    return render(request, 'index_6.html', context)


def index_7_1(request: HttpRequest):
    client_data = utils.get_main_client_front_data(request)
    context = {
        **client_data,
    }
    return render(request, 'index_7_1.html', context)


def index_7_2(request: HttpRequest):
    client_data = utils.get_main_client_front_data(request)
    context = {
        **client_data,
    }
    return render(request, 'index_7_2.html', context)
