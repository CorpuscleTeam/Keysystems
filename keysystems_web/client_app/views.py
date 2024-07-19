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

    client_data = utils.get_main_client_front_data(request)
    context = {
        **client_data
    }
    return render(request, 'index_4_1.html', context)


def index_4_2(request: HttpRequest):
    context = {}
    return render(request, 'index_4_2.html', context)
